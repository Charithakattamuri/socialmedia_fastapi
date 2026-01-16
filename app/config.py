from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Add DATABASE_URL as the primary way (Render provides this)
    database_url: Optional[str] = None
    
    # Make all individual database fields OPTIONAL with defaults
    database_username: Optional[str] = "postgres"
    database_password: Optional[str] = "password"
    database_hostname: Optional[str] = "localhost"
    database_port: Optional[str] = "5432"
    database_name: Optional[str] = "fastapi"
    
    # Keep these as they are
    secret_key: str = "your-very-secure-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        
    def get_database_url(self):
        """Get database URL - prefer DATABASE_URL if available"""
        if self.database_url:
            return self.database_url
        # Fallback to building from individual parts
        return f"postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}"

settings = Settings()