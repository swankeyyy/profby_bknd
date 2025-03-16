class Settings:
    DB_URL = 'postgresql+asyncpg://db:db@localhost:5432/db'
    DB_ECHO = True

    URL = "127.0.0.1:8000"

    API_PREFIX = "/api"

    REVIEWS_STORAGE = "../images/reviews"


settings = Settings()