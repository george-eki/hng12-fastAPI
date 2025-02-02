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

**Setup Instructions**

1 Clone the Repository

git clone https://github.com/yourusername/hng12-fastapi.git
cd hng12-fastapi

2 Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3 Install Dependencies

pip install -r requirements.txt

4 Run the API Locally

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Test in browser: http://127.0.0.1:8000

**Deployment Instructions (Render)**

Push your code to GitHub:

git add .
git commit -m "Initial commit"
git push origin main

Go to Render → New Web Service → Connect GitHub Repo.

Set the build settings:

Runtime: Python

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port 10000

Deploy and get your public API URL (https://hng12-fastapi-7uya.onrender.com/).

**Reference Link**

Learn more about FastAPI and backend development: Python Developers


**License**

This project is open-source and free to use.
