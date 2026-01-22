from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = ""

settings = Settings()

# move logic OUTSIDE the class
def get_database_url():
    if not settings.DATABASE_URL:
        return "sqlite:///./socialmedia.db"

    if settings.DATABASE_URL.startswith("postgres://"):
        return settings.DATABASE_URL.replace(
            "postgres://", "postgresql://", 1
        )

    return settings.DATABASE_URL
