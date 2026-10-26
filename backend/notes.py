from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Note, User
from schemas import NoteIn, NoteOut
from security import get_current_user

# Every endpoint in this file needs a logged-in user.
router = APIRouter(prefix="/notes", tags=["notes"])


def get_own_note_or_404(note_id: int, user: User, db: Session) -> Note:
    """Returns the note only if it belongs to the logged-in user."""
    note = db.get(Note, note_id)
    if note is None or note.user_id != user.id:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("", response_model=list[NoteOut])
def list_notes(
    user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    query = select(Note).where(Note.user_id == user.id).order_by(Note.id)
    return db.scalars(query).all()


@router.post("", response_model=NoteOut, status_code=201)
def create_note(
    note: NoteIn,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_note = Note(title=note.title, content=note.content, user_id=user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/{note_id}", response_model=NoteOut)
def get_note(
    note_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_own_note_or_404(note_id, user, db)


@router.put("/{note_id}", response_model=NoteOut)
def update_note(
    note_id: int,
    changes: NoteIn,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    note = get_own_note_or_404(note_id, user, db)
    note.title = changes.title
    note.content = changes.content
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    note = get_own_note_or_404(note_id, user, db)
    db.delete(note)
    db.commit()
