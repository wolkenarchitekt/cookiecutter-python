from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.package_name}}',
    description='{{cookiecutter.description}}',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'typer',
    ],
    entry_points={
        "console_scripts": ["{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.main:main"]
    },        
    {%- if cookiecutter.python_version %}
    python_requires='>={{cookiecutter.python_version}}'
    {%- endif %}
)
