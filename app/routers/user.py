from .. import models, schemas
import bcrypt
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
import app

router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a new user with bcrypt password hashing"""
    print(f"Creating user: {user.email}")
    print(f"Password: '{user.password}' ({len(user.password)} chars)")
    try:
        # Direct bcrypt hashing - NO PASSLIB
        password_bytes = user.password.encode('utf-8')
        
        # Debug print
        print(f"Password bytes length: {len(password_bytes)}")
        
        # Generate salt and hash
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)
        hashed_password = hashed_bytes.decode('utf-8')
        
        print(f"Hashed password (first 20 chars): {hashed_password[:20]}...")
        
        # Create user
        new_user = models.User(
            email=user.email,
            password=hashed_password
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        print(f"User created successfully: {new_user.id}")
        return new_user
    except Exception as e:
        print(f"Error creating user: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )  
       
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db),response: Response = schemas.UserOut):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return user 