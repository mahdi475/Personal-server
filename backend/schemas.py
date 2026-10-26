from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    """What the client sends to register."""

    username: str = Field(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    """What the API sends back about a user. Never includes the password."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    created_at: datetime


class Token(BaseModel):
    """The login response."""

    access_token: str
    token_type: str = "bearer"


class NoteIn(BaseModel):
    """What the client sends when creating or updating a note."""

    title: str = Field(min_length=1, max_length=200)
    content: str = ""


class NoteOut(NoteIn):
    """What the API sends back."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
