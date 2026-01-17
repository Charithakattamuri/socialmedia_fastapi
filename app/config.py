# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = ""
    
    # Other settings...
    
    def get_database_url(self):
        """Get database URL with proper formatting."""
        if not self.DATABASE_URL:
            # Fallback for local development
            return "sqlite:///./socialmedia.db"
        
        # Handle Heroku's postgres:// format if needed
        if self.DATABASE_URL.startswith("postgres://"):
            return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)
        
        return self.DATABASE_URL

settings = Settings()