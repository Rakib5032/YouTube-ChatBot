from youtube_transcript_api import(
    YouTubeTranscriptApi,
    TranscriptsDisabled
)

def load_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()
        
        transcript_list = ytt_api.fetch(
            video_id,
            languages=['en']
        )
        
        full_transcript = " ".join(
            [item.text for item in transcript_list]
        )
        return{
            "success": True,
            "transcript": full_transcript
        }
        
    except TranscriptsDisabled:
        return{
            'success': False,
            'message': 'No captions available'
        }
    except Exception as e:
        return{
            'success': False,
            'message': str(e)
        }