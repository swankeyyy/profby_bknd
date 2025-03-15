class Settings:
    DB_URL = 'postgresql+asyncpg://db:db@localhost:5432/db'
    DB_ECHO = True

    API_PREFIX = "/api"

    CONTACTS_STORAGE = "../images/reviews"


settings = Settings()