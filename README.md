# Postly — Social Media Frontend

**Stack:** Plain HTML/CSS/JS connected to your FastAPI + PostgreSQL backend

---

## 📁 Files

```
frontend/
├── login.html        ← Login & Sign Up
├── index.html        ← Post feed (view, search, vote, delete)
└── create-post.html  ← Create new post / Edit existing post
```

---

## ⚠️ IMPORTANT — Fix CORS in main.py

Your backend currently blocks all frontend requests.
Open your `main.py` and change the origins to allow your frontend:

```python
# CHANGE THIS:
origins = ["https://www.google.com", "https://www.youtube.com"]

# TO THIS:
origins = ["*"]
```

Without this change, the frontend cannot talk to your backend.

---

## 🚀 How to Run

**1. Start your backend** (in your backend folder with venv activated):
```bash
uvicorn app.main:app --reload
```

**2. Open the frontend in VS Code with Live Server:**
- Right-click `login.html` → Open with Live Server

Frontend runs at → http://127.0.0.1:5500/login.html

---

## ✅ Features

| Page | Features |
|------|----------|
| login.html | Login with email/password, Sign up, JWT token stored in localStorage |
| index.html | View all posts with vote counts, search posts, vote/unvote, delete own posts, edit own posts |
| create-post.html | Create new post, edit existing post, publish/draft toggle |

---

## 🔌 API Endpoints Used

| Method | Endpoint | Used in |
|--------|----------|---------|
| POST | /login | login.html |
| POST | /users/ | login.html (signup) |
| GET | /posts/ | index.html |
| POST | /posts/ | create-post.html |
| PUT | /posts/{id} | create-post.html (edit) |
| DELETE | /posts/{id} | index.html |
| POST | /vote/ | index.html |
| GET | /users/{id} | index.html (navbar email) |
