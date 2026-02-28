FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir .

COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port","8000" ]
