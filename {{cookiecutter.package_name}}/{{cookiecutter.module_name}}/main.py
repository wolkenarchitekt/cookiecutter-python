import typer

typer_app = typer.Typer()


@typer_app.command()
def command1():
    print("Command 1")


@typer_app.command()
def command2():
    print("Command 2")


def main():
    typer_app()


if __name__ == "__main__":
    main()
