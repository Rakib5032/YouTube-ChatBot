from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_transcript(transcript: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
    )
    
    chunks = splitter.create_documents([transcript])
    
    return chunks