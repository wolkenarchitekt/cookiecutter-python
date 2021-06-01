from typer.testing import CliRunner

from {{cookiecutter.module_name}}.main import typer_app

runner = CliRunner()


def test_hello_world():
    result = runner.invoke(typer_app, ["create", "johndoe"])
    assert result.exit_code == 1
