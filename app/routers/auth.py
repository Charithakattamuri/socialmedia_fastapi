from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt
from .. import database, schemas, models, oauth2

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    # 1. Find user by email
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # 2. Verify password with bcrypt
    try:
        # Convert to bytes for bcrypt
        password_bytes = user_credentials.password.encode('utf-8')
        hashed_bytes = user.password.encode('utf-8')
        
        # Check if password matches
        if not bcrypt.checkpw(password_bytes, hashed_bytes):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
            
    except Exception:
        # If bcrypt fails (invalid hash format)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # 3. Login successful

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}