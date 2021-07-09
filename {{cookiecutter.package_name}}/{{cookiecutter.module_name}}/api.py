from fastapi import FastAPI

from {{cookiecutter.module_name}}.routes import router
from {{cookiecutter.module_name}}.settings import Settings


def get_application() -> FastAPI:
    settings = Settings()
    application = FastAPI(title=settings.title)
    application.include_router(router)
    return application


fastapi_app = get_application()
