FROM python{%- if cookiecutter.python_version %}:{{ cookiecutter.python_version }}{%- endif %}-slim

# Required for packages from Github
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/code

WORKDIR /code
COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /code

# Allow overriding source files via volumes
RUN mkdir -p $(python -m site --user-site)
RUN cd $(python -m site --user-site) && python /code/setup.py develop

# Configure IPython (set old-style completion, enable autoreload extension)
COPY config/ipython/ipython_config.py /root/.ipython/profile_default/
COPY config/ipython/startup.py /root/.ipython/profile_default/startup/
