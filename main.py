from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the directory for templates
templates = Jinja2Templates(directory="templates")

# MongoDB connection
conn = MongoClient("mongodb+srv://pr2125116:Rcc1234@fast-api-practice.e9pbm.mongodb.net/notes")



# Route to return JSON response
@app.get("/items/{item_id}")
def read_item_json(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
