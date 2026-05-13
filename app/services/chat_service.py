from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from app.services.retriver import retrieve_docs
from app.models.model import chat_model


# FORMAT CONTEXT
def format_context(docs):
    # for doc in docs:
        # print(doc.page_content)
        # print("\n-----------------\n")
        
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

# PROMPT
prompt = PromptTemplate(

    template="""
        You are a helpful assistant.

        Answer ONLY from the provided
        transcript context.

        If the context is insufficient,
        just say you don't have enough Information.

        Context:
        {context}

        Question:
        {question}
        """,

            input_variables=[
                "context",
                "question"
            ]
)

# PARALLEL CHAIN
parallel_chain = RunnableParallel({
    "context":RunnableLambda(retrieve_docs) | RunnableLambda(format_context),
    "question":RunnablePassthrough()
})

# PARSER
parser = StrOutputParser()

# MAIN CHAIN
main_chain = (
    parallel_chain | prompt | chat_model | parser
)

# ASK QUESTION
def ask_question(question: str):

    response = main_chain.invoke(question)

    return {
        "success": True,
        "answer": response,
    }