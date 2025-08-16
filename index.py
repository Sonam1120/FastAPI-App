from fastapi import FastAPI
from routes.note import note
# from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pymango import MangoClient


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates"
                            )
app = FastAPI()
app.include_router(note)


@note.post("/")
def add_note(note: Note):
    inserted_note = conn.notes.notes.insert_one(dict(note))
    return noteEntity(inserted_note)

