"""
FastAPI Example - Creating an Item
-----------------------------------
Purpose: Demonstrates basic POST request with Pydantic model
- Uses BaseModel for data validation
- POST endpoint to create an item
- Returns confirmation message

Run: uvicorn example:app --reload
Test: curl -X POST "http://localhost:8000/item" \
      -H "Content-Type: application/json" \
      -d '{"id": 1, "name": "Laptop"}'
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for Item (validates incoming data)
class Item(BaseModel):
    id: int
    name: str

@app.post("/item")
def create_item(item: Item):
    return {"message": f"Item {item.name} created successfully."}