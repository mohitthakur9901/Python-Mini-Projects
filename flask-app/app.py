from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# In-memory database (list of dictionaries)
items_db = []


class Item(BaseModel):
    id: int
    BookName: str
    description: Optional[str] = None
    Author: str



# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing_item in items_db:
        if existing_item["id"] == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items_db.append(item.dict())
    return item

# Read all items
@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]

# Read a single item by ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item by ID
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            items_db[index] = item.dict()
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by ID
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")




if __name__ == "__main__":
    uvicorn.run(app)