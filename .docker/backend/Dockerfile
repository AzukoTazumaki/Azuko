FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY requirements.txt project.py db.py ./

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python -m pip install --upgrade pip && pip install -r requirements.txt &&  \
    apk --purge del .build-deps

CMD ["uvicorn", "project:app", "--host", "0.0.0.0", "--port", "80"]