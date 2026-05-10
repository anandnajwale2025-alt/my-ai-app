"""
GET Request Example
-------------------
Purpose: Retrieve/read data from the server
- No request body needed
- Data is fetched, not modified
- Used for reading information only
- Example: Fetching a list of items, user profile, etc.

Run: uvicorn get_response:app --reload
Test: curl http://localhost:8000/responses
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/responses")
async def get_responses():
    return [
        {"id": 1, "user_input": "Summarize AI news", "output": "AI news summarized..."},
        {"id": 2, "user_input": "Generate code snippet", "output": "Python snippet..."}
    ]
