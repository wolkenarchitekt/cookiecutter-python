import logging

from sqlalchemy.orm.session import Session

from {{cookiecutter.module_name}}.database.models import UserModel

logger = logging.getLogger(__name__)


def get_users(session: Session):
    query = session.query(UserModel)
    return query
