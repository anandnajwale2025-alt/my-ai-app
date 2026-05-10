"""
Path Parameter Example
----------------------
Purpose: Demonstrate using path parameters to identify resources
- Path parameters are part of the URL path: /responses/{response_id}
- They are REQUIRED (not optional)
- Used to identify a specific resource
- Enclosed in curly braces {} in the route
- Automatically validated and converted to specified type

Difference from Query Parameters:
- Path: /responses/1 (required, part of path)
- Query: /responses?id=1 (optional, after '?')

Run: uvicorn path_parameter:app --reload
Test: curl http://localhost:8000/responses/1
Test Invalid: curl http://localhost:8000/responses/999
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

# Example in-memory storage for AI outputs
responses = [
    {"id": 1, "user_input": "Summarize AI news", "output": "AI news summarized...", "model": "gpt-4"},
    {"id": 2, "user_input": "Generate code snippet", "output": "Python snippet...", "model": "gpt-3.5"}
]

# Path parameter: {response_id} is required and part of the URL
@app.get("/responses/{response_id}")
async def get_response(response_id: int):
    """
    Retrieve a specific response by ID using path parameter.
    - response_id: Must be an integer (FastAPI validates this)
    - Returns 404 if not found
    """
    for resp in responses:
        if resp["id"] == response_id:
            return resp
    raise HTTPException(status_code=404, detail="Response not found")
