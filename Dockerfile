FROM tiangolo/uvicorn-gunicorn:latest

WORKDIR /app

COPY static templates models names.py lyrics.py project.py Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip && pip install pipenv

RUN pipenv --python /usr/local/bin/python3 install

EXPOSE 8000

CMD ["uvicorn", "project:app", "--host", "0.0.0.0", "--port", "8000"]