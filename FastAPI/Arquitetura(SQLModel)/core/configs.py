from pydantic import BaseSettings

class Settings(BaseSettings):
    
    API_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://thiago:123456@localhost:5439/postgres'

    class Config:
        case_sensitive = True

settings : Settings = Settings() 