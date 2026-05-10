"""
PUT Request Example
-------------------
Purpose: Fully update/replace an existing resource
- Requires ID in URL path to identify resource
- Requires complete request body (all fields)
- Replaces the entire resource
- Example: Updating all details of a user profile

Run: uvicorn put_response:app --reload
Test: curl -X PUT "http://localhost:8000/responses/1" \
      -H "Content-Type: application/json" \
      -d '{"user_input": "Updated", "model": "GPT-4"}'
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model for AI prompts (all fields required for full update)
class Prompt(BaseModel):
    user_input: str
    model: str

@app.put("/responses/{id}")
async def update_response(id: int, prompt: Prompt):
    return {"message": f"AI output {id} updated with new input: '{prompt.user_input}'."}