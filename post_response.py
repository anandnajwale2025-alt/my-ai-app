"""
POST Request Example
--------------------
Purpose: Create new resources on the server
- Requires request body with data
- Creates something new (doesn't update existing)
- Body is validated using Pydantic models
- Example: Creating a new user, submitting a form, etc.

Run: uvicorn post_response:app --reload
Test: curl -X POST "http://localhost:8000/responses" \
      -H "Content-Type: application/json" \
      -d '{"user_input": "Hello", "model": "GPT-4"}'
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model for AI prompts (defines required fields and their types)
class Prompt(BaseModel):
    user_input: str
    model: str

@app.post("/responses")
async def create_response(prompt: Prompt):
    return {"message": f"AI model '{prompt.model}' generated output for your input: '{prompt.user_input}'."}