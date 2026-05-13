from fastapi import APIRouter

from app.services.transcript_loader import (
    load_transcript
)

from app.routes.url_loader import (
    extract_video_id
)

from app.services.chunk_docs import (
    chunk_transcript
)

from app.services.vector_store import (
    create_vector_store
)

from app.services.chat_service import (
    ask_question
)

router = APIRouter()


# PROCESS VIDEO
@router.post("/process-video")
async def process_video(data: dict):

    youtube_url = data.get("url")

    if not youtube_url:

        return {
            'success': False,
            'message': 'YouTube URL is required'
        }

    video_id = extract_video_id(
        youtube_url
    )

    if not video_id:

        return {
            'success': False,
            'message': 'Invalid YouTube URL'
        }

    transcript_result = load_transcript(
        video_id
    )

    if transcript_result["success"]:

        chunks = chunk_transcript(
            transcript_result["transcript"]
        )

        # CREATE VECTOR STORE
        create_vector_store(chunks)

        return {

            'success': True,

            'message':
                'Your Video is ready to chat!'
        }

    else:
        return transcript_result

# ASK QUESTION
@router.post("/ask")
async def ask(data: dict):

    query = data.get("question")

    if not query:

        return {

            "success": False,

            "message": "Question required"
        }

    result = ask_question(query)

    return result