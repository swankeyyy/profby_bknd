class Settings:
    DB_URL: str = "postgresql+asyncpg://profby:profby@localhost:5432/profby"
    DB_ECHO: bool = True
    
    URL: str = "127.0.0.1:8000"
    API_PREFIX: str = "/api"
    
    REVIEWS_STORAGE: str = "./images/reviews"
    PROFESSIONS_STORAGE: str = "./images/professions"
    SECTIONS_STORAGE: str = "./images/sections"
    
    SECRET_KEY: str = "ahjdhjkashdjkashdjkashdkjahdk" 




settings = Settings()