from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

base_url='https://openrouter.ai/api/v1'
api_key=os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(
    model = 'gpt-4o-mini',
    base_url=base_url,
    api_key=api_key
)

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-small',
    base_url=base_url,
    api_key=api_key
)
