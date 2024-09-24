from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items_list = {
    "1": "abacate",
    "2": "maçã",
    "3": "abacaxi",
    "4": "banana",
    "5": "melancia",
    "6": "melão",
    "7": "morango",
    "8": "laranja",
}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items")
async def list_items(q: Union[str, None] = None):
    if q:
        if q in items_list.values():
            return {"tem": q}
    return {**items_list}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}