from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from config import settings
from database import get_db
from models import User

ALGORITHM = "HS256"

# Argon2 turns a password into a hash that can't be turned back.
password_hasher = PasswordHash.recommended()

# Tells FastAPI (and the Swagger "Authorize" button) where to log in.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return password_hasher.verify(password, password_hash)


def create_access_token(user_id: int) -> str:
    """Creates a signed token that says "this is user X" and expires."""
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_minutes
    )
    payload = {"sub": str(user_id), "exp": expires}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """Reads the token from the request and returns the logged-in user."""
    invalid = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        user_id = int(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError):
        raise invalid

    user = db.get(User, user_id)
    if user is None:
        raise invalid
    return user
