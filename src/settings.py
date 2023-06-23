from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_user: str = Field(env="POSTGRES_USER")
    db_password: str = Field(env="POSTGRES_PASSWORD")
    db_name: str = Field(env="POSTGRES_DB")
    db_host: str = Field(env="POSTGRES_HOST", default="localhost")
    db_port: int = Field(env="POSTGRES_PORT", default=5432)
    debug: bool = Field(env="DEBUG", default=True)
