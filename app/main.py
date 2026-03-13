from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas
from .database import engine, get_db, Base
from .routers import post, user, auth, vote
from .config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my api!!!"}

    


