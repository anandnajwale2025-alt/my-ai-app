"""
PATCH Request Example
---------------------
Purpose: Partially update an existing resource
- Requires ID in URL path to identify resource
- Only send fields you want to update (not all fields)
- Uses Optional fields in Pydantic model
- Example: Updating just email or just name of a user

Run: uvicorn patch_response:app --reload
Test: curl -X PATCH "http://localhost:8000/responses/1" \
      -H "Content-Type: application/json" \
      -d '{"user_input": "Only updating this field"}'
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model for partial updates (all fields are Optional)
class PromptPatch(BaseModel):
    user_input: Optional[str] = None
    model: Optional[str] = None

@app.patch("/responses/{id}")
async def patch_response(id: int, prompt: PromptPatch):
    return {"message": f"AI output {id} partially updated with: {prompt.model_dump(exclude_none=True)}."}
