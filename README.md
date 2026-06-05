# SkillForge AI

SkillForge AI is an AI-powered career preparation platform built using Django, FastAPI, Groq AI, MySQL, HTML, CSS, JavaScript, and Tailwind CSS.

The platform helps students and job seekers improve their skills, prepare for interviews, build stronger resumes, and learn with the assistance of AI.

---

## Features

### AI Interview Practice

* Python Developer Interviews
* Django Developer Interviews
* Frontend Developer Interviews
* HR Interviews
* AI-generated questions
* AI answer evaluation
* Score calculation
* Performance feedback

### AI Assistant

* ChatGPT-style AI chatbot
* Persistent chat history
* Create new chats
* Delete old chats
* Technical learning support
* Interview preparation assistance

### Resume AI

* Upload PDF resumes
* Extract resume content
* Analyze projects, skills, internships, and experience
* Generate personalized interview questions based on resume content
* AI-powered resume interview simulation

### Dashboard

* Centralized access to all platform features
* Clean and user-friendly interface

### User Management

* User Registration
* User Login
* User Logout
* Secure authentication system

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Tailwind CSS
* JavaScript

### Backend

* Django
* FastAPI

### Database

* MySQL

### AI Integration

* Groq API
* Llama 3.1 8B Instant

### Additional Libraries

* PyPDF2
* Requests
* Python Dotenv

---

## Project Structure

```text
SkillForge_AI/
│
├── chatbot/
├── dashboard/
├── interviews/
├── resume_ai/
├── users/
├── templates/
├── static/
├── fastapi_service/
├── config/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shalon2255/SkillForge_AI.git
cd SkillForge_AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

### Run Django Server

```bash
python manage.py runserver
```

### Run FastAPI Service

```bash
uvicorn fastapi_service.main:app --reload --port 8001
```

---

## Future Improvements

* Resume score analysis
* Learning roadmap generation
* Job recommendation system
* AI coding challenges
* Performance analytics dashboard
* Interview report downloads

---

## Author

**Shalon Rodrigs**

BCA Graduate | Python Developer | Django Developer | AI Enthusiast

GitHub:
https://github.com/shalon2255
