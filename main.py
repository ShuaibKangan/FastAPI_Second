from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()

@dataclass
class pet:
    id: int
    name: str
    breed: str
    gender: str
    age: int

pets: list[pet] = [
    pet(1, "ben", "dalmatian", "male", 2),
    pet(2, "Rosey", "poodle", "female", 1),
]

@app.get("/")
def home():
    return {"message": "Suuuu~p"}

@app.get("/pets")
def pet_range():
    pet_names = []

    for item in pets:
        print(item.name)
        pet_names.append(item.name)
    return pet_names
