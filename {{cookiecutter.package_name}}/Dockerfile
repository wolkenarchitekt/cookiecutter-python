FROM python{%- if cookiecutter.python_version %}:{{ cookiecutter.python_version }}{%- endif %}-slim

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code

WORKDIR /code
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code
