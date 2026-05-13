from langchain_community.vectorstores import FAISS
from app.models.model import embeddings

def create_vector_store(chunks):
    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )
    vector_store.save_local(
        "app/data/faiss_index"
    )
    
    return vector_store