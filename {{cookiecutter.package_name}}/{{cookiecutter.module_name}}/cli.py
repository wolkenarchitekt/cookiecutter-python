import logging

import typer

logger = logging.getLogger(__name__)

typer_app = typer.Typer()


@typer_app.command()
def create(username: str):
    logger.debug("About to create a user")
    logger.info(f"Deleting user: {username}")
    logger.debug("Just created a user")


@typer_app.command()
def delete(username: str):
    logger.debug("About to delete a user")
    logger.info(f"Deleting user: {username}")
    logger.debug("Just deleted a user")


@typer_app.callback()
def main(verbose: int = typer.Option(0, "--verbose", "-v", count=True)):
    if verbose == 0:
        logging.basicConfig(level=logging.WARN)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif verbose > 1:
        logging.basicConfig(level=logging.DEBUG)
