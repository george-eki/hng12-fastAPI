**HNG12 Backend Task - Public API**

Project Overview

This is a simple public API developed as part of the HNG12 Backend Internship. The API returns basic information in JSON format, including:

Registered Email (used in HNG12 Slack workspace)

Current Datetime (in ISO 8601 format, UTC timezone)

GitHub Repository URL


**Tech Stack**

Python 3.12

FastAPI (Lightweight web framework)

Uvicorn (ASGI server)

Render (Hosting & Deployment)


**API Endpoint**

GET /

Response Format (200 OK):
{
  
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "
}

**Reference Link**

Learn more about FastAPI and backend development: Python Developers


**License**

This project is open-source and free to use.
