"""
Complete REST API Example - All HTTP Methods
---------------------------------------------
This file demonstrates all 5 main HTTP methods (CRUD operations):

1. GET    - READ: Retrieve data (no body)
2. POST   - CREATE: Create new resource (full body required)
3. PUT    - UPDATE: Replace entire resource (ID + full body)
4. PATCH  - UPDATE: Modify part of resource (ID + partial body)
5. DELETE - DELETE: Remove resource (ID only)

Key Differences:
- GET & DELETE: No request body needed
- POST: No ID needed (creates new resource)
- PUT: All fields required in body (full replacement)
- PATCH: Optional fields in body (partial update)

Run: uvicorn all_rest_methods:app --reload
Visit: http://localhost:8000/docs (FastAPI auto-generated documentation)
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model for AI prompts (used for POST and PUT)
class Prompt(BaseModel):
    user_input: str
    model: str

# Model for partial updates (used for PATCH)
class PromptPatch(BaseModel):
    user_input: Optional[str] = None
    model: Optional[str] = None

# GET - Retrieve all responses
@app.get("/responses")
async def get_responses():
    return [
        {"id": 1, "user_input": "Summarize AI news", "output": "AI news summarized..."},
        {"id": 2, "user_input": "Generate code snippet", "output": "Python snippet..."}
    ]

# POST - Create a new response
@app.post("/responses")
async def create_response(prompt: Prompt):
    return {"message": f"AI model '{prompt.model}' generated output for your input: '{prompt.user_input}'."}

# PUT - Update existing response (full update)
@app.put("/responses/{id}")
async def update_response(id: int, prompt: Prompt):
    return {"message": f"AI output {id} updated with new input: '{prompt.user_input}'."}

# PATCH - Partially update existing response
@app.patch("/responses/{id}")
async def patch_response(id: int, prompt: PromptPatch):
    return {"message": f"AI output {id} partially updated with: {prompt.model_dump(exclude_none=True)}."}

# DELETE - Remove a response
@app.delete("/responses/{id}")
async def delete_response(id: int):
    return {"message": f"AI output {id} removed from the system."}
