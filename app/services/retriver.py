from langchain_community.vectorstores import FAISS

from app.models.model import embeddings


def retrieve_docs(query: str):

    # LOAD LATEST VECTOR STORE
    vector_store = FAISS.load_local(

        "app/data/faiss_index",

        embeddings,

        allow_dangerous_deserialization=True
    )

    # CREATE NEW RETRIEVER
    retriever = vector_store.as_retriever(

        search_type="similarity",

        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(query)

    return docs