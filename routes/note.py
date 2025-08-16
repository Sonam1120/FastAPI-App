from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),   
            "note": doc["note"],
            "title": doc["item"],
            "desc": doc["dese"],
            "important": doc["important"],
        })

    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post('/')
async def create_item(request: Request):
    form = await request.form()
    formdict = dict(form)
    formdict["important"] = True if formdict.get("important") == 'on' else False
    
    conn.notes.notes.insert_one(formdict)
    return {"Success": True}


@note.put("/{id}")
async def update_item(id: str, request: Request):
    form = await request.form()
    formdict = dict(form)
    formdict["important"] = True if formdict.get("important") == 'on' else False
    
    conn.notes.notes.update_one({"_id": ObjectId(id)}, {"$set": formdict})
    return {"Success": True, "message": f"Note {id} updated"}


# ✅ DELETE (Delete Note)
@note.delete("/{id}")
async def delete_item(id: str):
    conn.notes.notes.delete_one({"_id": ObjectId(id)})
    return {"Success": True, "message": f"Note {id} deleted"}