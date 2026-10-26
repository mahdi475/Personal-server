from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Note
from schemas import NoteIn, NoteOut


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once when the API starts: creates tables that don't exist yet.
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Personal Server API", lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Mahdi's Personal Server API is running!"}


@app.get("/health")
def health(db: Session = Depends(get_db)):
    """Checks that the API can talk to the database."""
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=503, detail="Database unavailable")
    return {"status": "ok", "database": "ok"}


def get_note_or_404(note_id: int, db: Session) -> Note:
    note = db.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.get("/notes", response_model=list[NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return db.scalars(select(Note).order_by(Note.id)).all()


@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(note: NoteIn, db: Session = Depends(get_db)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    return get_note_or_404(note_id, db)


@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, changes: NoteIn, db: Session = Depends(get_db)):
    note = get_note_or_404(note_id, db)
    note.title = changes.title
    note.content = changes.content
    db.commit()
    db.refresh(note)
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = get_note_or_404(note_id, db)
    db.delete(note)
    db.commit()
