"""
DELETE Request Example
----------------------
Purpose: Remove/delete a resource from the server
- Requires ID in URL path to identify resource
- No request body needed
- Permanently removes the resource
- Example: Deleting a user account, removing a post, etc.

Run: uvicorn delete_response:app --reload
Test: curl -X DELETE "http://localhost:8000/responses/1"
"""

from fastapi import FastAPI

app = FastAPI()

@app.delete("/responses/{id}")
async def delete_response(id: int):
    return {"message": f"AI output {id} removed from the system."}
