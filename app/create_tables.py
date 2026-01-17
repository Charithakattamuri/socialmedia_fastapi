from app.database import Base, engine
from app.models import Post, User, Vote  # Import all your models

def create_tables():
    print("Creating database tables...")
    print("Tables to create:")
    print("- Posts")
    print("- Users (users1)")
    print("- Votes")
    
    # This creates all tables defined in your models
    Base.metadata.create_all(bind=engine)
    
    print("✅ All tables created successfully!")
    print("Tables created:")
    print("1. posts - For blog posts")
    print("2. users1 - For user accounts")  
    print("3. votes - For post votes/likes")

if __name__ == "__main__":
    create_tables()