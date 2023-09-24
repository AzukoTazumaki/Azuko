ARG PYTHON_VERSION=3.10.10
FROM python:3.9.18-slim-bullseye as base

WORKDIR /app

COPY static templates names.py project.py Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip && pip install pipenv

RUN pipenv install --system --deploy

EXPOSE 8000

CMD ["uvicorn", "project:app", "--host", "0.0.0.0", "--port", "8000"]
