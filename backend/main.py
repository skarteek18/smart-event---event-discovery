
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User, Event, Booking, Ticket, Notification
from schemas import UserRegister, UserLogin, Token
from auth import (
    hash_password,
    verify_password,
    create_token,
    get_current_user
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartEvent API",
    description="Event Discovery & Ticket Booking System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SmartEvent API"
    }


# -------------------------
# USER AUTHENTICATION
# -------------------------

@app.post("/register")
def register(
    data: UserRegister,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "Registration successful"
    }


@app.post("/login", response_model=Token)
def login(
    data: UserLogin,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not
