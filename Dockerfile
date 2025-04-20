FROM python:3.12-slim

RUN apt update && apt install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -m django && \
    mkdir -p /app/static /app/media && \
    chown django:django /app/static /app/media

COPY --chown=django:django . .

ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PROD_RUN=1

# Collecting static
USER django
RUN python manage.py collectstatic --noinput

# Run Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120", "inventory.wsgi"]
