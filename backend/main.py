from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

import auth
import notes
from database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once when the API starts: creates tables that don't exist yet.
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Personal Server API", lifespan=lifespan)
app.include_router(auth.router)
app.include_router(notes.router)


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
