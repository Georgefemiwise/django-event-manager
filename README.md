# Event Management System

A Django-based event management system with JWT authentication.

## Features

- User roles: Admin and Event Organizer
- JWT Authentication
- Event management
- Category and tag system
- Admin approval workflow

## Installation

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run development server:
```bash
python manage.py runserver
```

## API Documentation

Available at `/api/` when running the development server.

## Environment Variables

Create `.env` file:
```
DJANGO_SECRET_KEY=your-secret-key-here
```
