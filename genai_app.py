
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key():
    # Try to read from Google Cloud Secret Manager if available
    try:
        import google.auth
        from google.cloud import secretmanager
        _, project_id = google.auth.default()
        client = secretmanager.SecretManagerServiceClient()
        secret_name = os.getenv("GEMINI_SECRET_NAME", "gemini-api-key")
        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception:
        # Fallback to environment variable
        return os.getenv("GEMINI_API_KEY")

GEMINI_API_KEY = get_gemini_api_key()

# Initialize the Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize FastAPI app
app = FastAPI(title="Summarizer API", version="1.0")

# Request and response models
class SummaryRequest(BaseModel):
    text: str
    max_length: Optional[int] = 153

class SummaryResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummaryResponse)
def summarize(request: SummaryRequest):
    try:
        prompt = f"Summarize the following text briefly in under {request.max_length} words:\n\n{request.text}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        summary = response.text.strip()
        return {"summary": summary}
    except Exception as e:
        print(f"Error during summarization: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
    