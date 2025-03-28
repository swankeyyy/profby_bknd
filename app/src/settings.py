class Settings:
    # Database settings
    DB_URL: str = "postgresql+asyncpg://profby:profby@localhost:5432/profby"
    DB_ECHO: bool = True
    
    # Server settings
    URL: str = "127.0.0.1:8000"
    API_PREFIX: str = "/api"
    
    # Storage settings (for fastapi_storage)
    REVIEWS_STORAGE: str = "./images/reviews"
    PROFESSIONS_STORAGE: str = "./images/professions"
    SECTIONS_STORAGE: str = "./images/sections"
    
    # Default developers secret key for password hashing
    SECRET_KEY: str = "ahjdhjkashdjkashdjkashdkjahdk" 



# Create an instance of the Settings class
settings = Settings()