FROM python:3.11-alpine3.18

WORKDIR /srv

# UPDATE PACKAGES
RUN apk update && apk upgrade
RUN apk add build-base python3-dev libffi-dev

# SET ENVS
ENV TZ America/Sao_Paulo
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8

# SERVICE
COPY . .

# INSTALL POETRY AND CONFIGURE
RUN python3 -m pip install -q --upgrade pip
RUN pip install -q poetry
RUN poetry config virtualenvs.create false

# INSTALL PROJECT DEPENDENCIES
RUN poetry install --only=main --no-cache --no-root

# RUN
CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
