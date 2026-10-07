

SmartEvent – Event Discovery & Ticket Booking System

SmartEvent is a full-stack web application that allows users to discover events, book tickets, view digital tickets with QR codes, and receive event notifications.

🚀 Technology Stack

Backend

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL / MySQL / SQLite
- Pydantic
- JWT Authentication
- bcrypt
- QR Code Generation

Frontend

- React
- Vite
- Axios
- HTML
- CSS
- JavaScript

---

📌 Project Modules

Module 1 – User Authentication

Users can create an account and securely log in.

Features:

- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- User Profile
- Protected Routes
- Input Validation

Users Table:

Field| Description
id| User ID
username| Username
email| User email
hashed_password| Encrypted password
created_at| Account creation time

---

Module 2 – Event Discovery

Users can browse and search for available events.

Features:

- View all events
- View event details
- Search events by title
- Filter events by category
- Display event date, location and ticket price
- Display event banner image

Event Categories:

- Music
- Tech
- Sports
- Business

Events Table:

Field| Description
id| Event ID
title| Event title
description| Event description
category| Event category
location| Event location
event_date| Event date
ticket_price| Ticket price
banner_image| Event image
created_at| Creation time

---

Module 3 – Ticket Booking

Users can book tickets for available events.

Features:

- Select ticket quantity
- Calculate total price automatically
- Check ticket availability
- Prevent booking when tickets are sold out
- View booking history
- Booking status management

Booking Status:

- PENDING
- CONFIRMED
- CANCELLED

Bookings Table:

Field| Description
id| Booking ID
user_id| User ID
event_id| Event ID
ticket_quantity| Number of tickets
total_price| Total booking amount
booking_status| Booking status
created_at| Booking time

---

Module 4 – QR Code Ticket System

After a successful booking, users receive a digital ticket.

Features:

- Generate unique ticket code
- Generate QR code
- Store QR code information
- Display event details
- Display ticket code
- Download digital ticket
- QR verification at event entry

Tickets Table:

Field| Description
id| Ticket ID
booking_id| Booking ID
ticket_code| Unique ticket code
qr_code_url| QR code location
created_at| Ticket creation time

---

Module 5 – Event Notifications

Users receive notifications related to their bookings and upcoming events.

Features:

- Booking confirmation notification
- Event reminder notification
- Notification list
- Unread notification count
- Mark notification as read

Notification Types:

- EVENT
- BOOKING
- SYSTEM

Notifications Table:

Field| Description
id| Notification ID
user_id| User ID
title| Notification title
message| Notification message
type| Notification type
is_read| Read status
created_at| Creation time

---

🎨 Frontend Pages

The React frontend contains the following pages:

1. Register Page
2. Login Page
3. Home / Events Listing Page
4. Event Details Page
5. Booking Confirmation Page
6. Booking History Page
7. Tickets Page
8. Notifications Page

Components

- Navbar
- EventCard
- TicketCard
- NotificationDropdown
- ProtectedRoute

---

🔐 Security

SmartEvent implements the following security features:

- JWT-based authentication
- Password hashing using bcrypt
- Protected booking routes
- Booking ownership validation
- Pydantic input validation
- Environment variables for sensitive configuration
- Proper HTTP error handling

---

🔄 Application Workflow

User
  ↓
Register / Login
  ↓
JWT Authentication
  ↓
Browse Events
  ↓
Search / Filter Events
  ↓
View Event Details
  ↓
Select Ticket Quantity
  ↓
Book Tickets
  ↓
Booking Confirmation
  ↓
Generate Digital Ticket
  ↓
Generate QR Code
  ↓
View Ticket
  ↓
Receive Notifications

---

📁 Project Structure

SmartEvent/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── auth.py
│   │   ├── dependencies.py
│   │   │
│   │   └── routers/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── events.py
│   │       ├── bookings.py
│   │       ├── tickets.py
│   │       └── notifications.py
│   │
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md

---

⚙️ Backend Setup

1. Clone the Repository

git clone <your-github-repository-url>
cd SmartEvent

2. Create Virtual Environment

python -m venv venv

3. Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Configure Environment Variables

Create a ".env" file:

DATABASE_URL=sqlite:///./smartevent.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

6. Run FastAPI

uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

---

⚛️ Frontend Setup

Open a new terminal:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

The React application will normally run at:

http://localhost:5173

---

🔗 API Integration

The frontend communicates with the FastAPI backend using Axios.

Example:

React Frontend
      ↓
    Axios
      ↓
FastAPI Backend
      ↓
   SQLAlchemy
      ↓
    Database

JWT tokens are stored in "localStorage" and attached to protected API requests.

---

📋 Main API Endpoints

Authentication

POST   /auth/register
POST   /auth/login
GET    /users/me

Events

GET    /events
GET    /events/{event_id}
GET    /events/category/{category}
GET    /events/search

Bookings

POST   /bookings
GET    /bookings/my-bookings
GET    /bookings/{booking_id}

Tickets

GET    /tickets
GET    /tickets/{ticket_id}

Notifications

GET    /notifications
PUT    /notifications/{notification_id}/read

---

🗄️ Database Relationships

Users
  │
  ├──────────< Bookings
  │                │
  │                └────────── Event
  │
  └──────────< Notifications

Bookings
   │
   └──────────< Tickets

- One user can have multiple bookings.
- One event can have multiple bookings.
- One booking belongs to one user and one event.
- A booking can generate digital tickets.
- A user can receive multiple notifications.

---

✅ Key Features

- User Registration and Login
- JWT Authentication
- Secure Password Hashing
- Event Discovery
- Event Search
- Category Filtering
- Ticket Booking
- Ticket Availability Validation
- Booking History
- Digital QR Tickets
- Event Notifications
- Protected Routes
- Responsive React UI
- FastAPI Swagger Documentation

---

🎯 Project Objective

The main objective of SmartEvent is to build a real-world full-stack event booking application while gaining practical experience in:

- REST API development
- Authentication and authorization
- Database relationships
- Booking workflows
- QR code generation
- React and FastAPI integration
- API validation
- Frontend state management
- Secure application development

---

👨‍💻 Project Status

Status: In Development

Project: SmartEvent – Event Discovery & Ticket Booking System

Backend: FastAPI

Frontend: React + Vite

Database: SQL