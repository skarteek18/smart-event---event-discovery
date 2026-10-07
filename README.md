# smart-event---event-discovery

SmartEvent is a full-stack event discovery and ticket booking application. Users can discover events, view event details, book tickets, receive digital QR tickets, and manage their bookings and notifications.
The project is developed using FastAPI for the backend and React + Vite for the frontend.
🛠️ Technologies Used
Backend
Python
FastAPI
SQLAlchemy
SQLite
Pydantic
JWT Authentication
bcrypt
QR Code
Frontend
React
Vite
Axios
React Router
JavaScript
CSS
📂 Project Structure
SmartEvent/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── requirements.txt
│   └── routers/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
│
├── ScreenShorts/
├── README.md
└── .gitignore
🚀 Features
1. User Authentication
User registration
User login
JWT authentication
Password hashing
Protected routes
User profile
2. Event Discovery
View all events
View event details
Search events
Filter by category
Display event image, date, location and price
3. Ticket Booking
Select ticket quantity
Check ticket availability
Calculate total price automatically
Book tickets
View booking history
Prevent booking when tickets are unavailable
4. QR Code Tickets
Generate unique ticket code
Generate QR code
Display digital ticket
View user's tickets
5. Notifications
Booking confirmation notification
Event notifications
View notifications
Mark notifications as read
⚙️ Backend Setup
Go to the backend folder:
cd backend
Create a virtual environment:
python -m venv venv
Activate it on Windows:
venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Start FastAPI:
uvicorn main:app --reload
Backend will run at:
http://127.0.0.1:8000
API documentation:
http://127.0.0.1:8000/docs
💻 Frontend Setup
Go to the frontend folder:
cd frontend
Install dependencies:
npm install
Start the React application:
npm run dev
Frontend will run at:
http://localhost:5173
🔐 Authentication Flow
Register
   ↓
Login
   ↓
JWT Token
   ↓
Store Token in localStorage
   ↓
Attach Token to API Requests
   ↓
Access Protected Routes
🎫 Booking Flow
Browse Events
      ↓
Select Event
      ↓
View Event Details
      ↓
Select Ticket Quantity
      ↓
Check Availability
      ↓
Confirm Booking
      ↓
Generate QR Ticket
      ↓
View Ticket
🗄️ Database Tables
The application uses the following tables:
Users
Events
Bookings
Tickets
Notifications
Users
id
username
email
hashed_password
created_at
Events
id
title
description
category
location
event_date
ticket_price
banner_image
created_at
Bookings
id
user_id
event_id
ticket_quantity
total_price
booking_status
created_at
Tickets
id
booking_id
ticket_code
qr_code_url
created_at
Notifications
id
user_id
title
message
type
is_read
created_at
🔒 Security
JWT-based authentication
Password hashing using bcrypt
Protected booking APIs
Booking ownership validation
Pydantic input validation
Secure environment configuration
Proper API error handling
📱 Frontend Pages
Register Page
Login Page
Home / Events Page
Event Details Page
Booking Confirmation Page
Booking History Page
Tickets Page
Notifications Page
🎯 Project Objective
The main objective of SmartEvent is to build a real-world full-stack event booking application and gain practical experience in:
REST API development
FastAPI
React integration
Database relationships
JWT authentication
Ticket booking workflows
QR code generation
API integration using Axios
Frontend routing
Protected routes
👨‍💻 Project
Project Name: SmartEvent – Event Discovery & Ticket Booking System
Backend: FastAPI + Python
Frontend: React + Vite
Database: SQLite
Authentication: JWT
