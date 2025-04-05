import os


class Settings:
    # Database settings
    DB_URL: str = os.environ.get("DB_URL")
    DB_ECHO: bool = bool(int(os.environ.get("DB_ECHO")))

    # Server settings
    URL: str = os.environ.get("URL")
    API_PREFIX: str = os.environ.get("API_PREFIX")

    # Storage settings (for fastapi_storage)
    REVIEWS_STORAGE: str = os.environ.get("REVIEWS_STORAGE")
    PROFESSIONS_STORAGE: str = os.environ.get("PROFESSIONS_STORAGE")
    SECTIONS_STORAGE: str = os.environ.get("SECTIONS_STORAGE")

    # Default developers secret key for password hashing
    SECRET_KEY: str = os.environ.get("SECRET_KEY")

    # Telegram bot settings
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    CHAT_ID: str = os.environ.get("CHAT_ID")


# Create an instance of the Settings class
settings = Settings()
