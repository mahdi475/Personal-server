from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteIn(BaseModel):
    """What the client sends when creating or updating a note."""

    title: str = Field(min_length=1, max_length=200)
    content: str = ""


class NoteOut(NoteIn):
    """What the API sends back."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
