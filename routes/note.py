from fastapi import APIRouter, Request, Form, HTTPException, status
from pydantic import BaseModel
from models.note import Note
from config.db import conn
from schemas.note import notesEntity
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging

note = APIRouter()

# Define the directory for templates
templates = Jinja2Templates(directory="templates")


# Pydantic model for input validation
class CreateNoteModel(BaseModel):
    title: str
    desc: str
    important: bool = False


# Route to render an HTML template
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  # Ensure ID is a string
            "title": doc["title"],
            "desc": doc["desc"],
            # "important": doc["important"]
        })
    return templates.TemplateResponse("item.html", {"request": request, "newDocs": newDocs})


@note.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(
        request: Request,
        title: str = Form(...),
        desc: str = Form(...),
        # important: str = Form(None)
):
    logging.info("Received form data: title=%s, desc=%s, important=%s", title, desc)  # Log form data

    # important_val = important == "on"

    new_note = CreateNoteModel(title=title, desc=desc)
    conn.notes.notes.insert_one(dict(new_note))
    return {"Success": True}
