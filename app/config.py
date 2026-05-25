from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "map-gateway-service"

    MAPY_API_KEY: str = ""

    MAPY_BASE_URL: str = "https://api.mapy.com/v1"

    class Config:
        env_file = ".env"


settings = Settings()