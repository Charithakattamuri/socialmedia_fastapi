# app/create_tables.py
from app.database import Base, engine
from app import models  # Make sure to import all your models here

# Import all your models so they're registered with Base
# Example: from app.models.user import User
# Example: from app.models.post import Post

def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()