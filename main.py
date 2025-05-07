# Define the FurnitureItem model
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# Define the FurnitureItem model
class FurnitureItem(BaseModel):
    id: int
    color: str
    title: str
    price: int
    isFavorite: bool
    furniture3dTitle: str
    category: str

# Function to load furniture data from the JSON file
def load_furniture_data():
    try:
        with open("furniture.json", "r") as file:
            data = file.read().strip()  # Read and strip whitespace/newlines
            if not data:
                print("The furniture.json file is empty.")
                return []  # Return an empty list
            return json.loads(data)  # Parse the JSON data
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return []  # Return an empty list in case of error
    except FileNotFoundError:
        print("Error: furniture.json file not found!")
        return []  # Return an empty list if the file is not found

# Endpoint to get all furniture items
@app.get("/furniture", response_model=List[FurnitureItem])
def get_furniture():
    return load_furniture_data()

# Endpoint to get a specific furniture item by ID
@app.get("/furniture/{item_id}", response_model=FurnitureItem)
def get_furniture_item(item_id: int):
    data = load_furniture_data()
    for item in data:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}  # Return error message if item is not found
