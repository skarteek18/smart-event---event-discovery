from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# =========================
# User Schemas
# =========================

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# Login Schema
# =========================

class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# =========================
# Event Schemas
# =========================

class EventCreate(BaseModel):
    title: str
    description: str
    category: str
    location: str
    event_date: datetime
    ticket_price: float
    banner_image: Optional[str] = None


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    event_date: datetime
    ticket_price: float
    banner_image: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# Booking Schemas
# =========================

class BookingCreate(BaseModel):
    event_id: int
    ticket_quantity: int


class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    ticket_quantity: int
    total_price: float
    booking_status: str
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# Ticket Schemas
# =========================

class TicketResponse(BaseModel):
    id: int
    booking_id: int
    ticket_code: str
    qr_code_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# =========================
# Notification Schemas
# =========================

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    type: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True