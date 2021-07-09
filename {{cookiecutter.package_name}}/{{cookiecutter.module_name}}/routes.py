from fastapi import APIRouter

from {{cookiecutter.module_name}}.routers import hello

router = APIRouter()
router.include_router(router=hello.router, tags=["hello"], prefix="/api/hello")
