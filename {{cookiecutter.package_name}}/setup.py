from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.package_name}}',
    description='{{cookiecutter.description}}',
    packages=find_packages(exclude=("tests",)),
    version='0.0.1',
    install_requires=[
        'pydantic==1.8.2',
        'python-dotenv==0.18.0',
        'typer==0.3.2',
    ],
    entry_points={
        "console_scripts": ["{{cookiecutter.cli_script}} = {{cookiecutter.module_name}}.cli:typer_app"]
    },        
    {%- if cookiecutter.python_version %}
    python_requires='>={{cookiecutter.python_version}}'
    {%- endif %}
)
