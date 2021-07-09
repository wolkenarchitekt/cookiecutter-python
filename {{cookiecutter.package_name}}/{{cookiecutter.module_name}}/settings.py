from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = "{{cookiecutter.description}}"
    database_url: str = "sqlite://"

    class Config:
        env_file = ".env"
