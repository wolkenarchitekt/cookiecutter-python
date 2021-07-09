from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = "{{cookiecutter.description}}"

    class Config:
        env_file = ".env"
