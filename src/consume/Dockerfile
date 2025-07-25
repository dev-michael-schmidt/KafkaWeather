FROM python:3.11-bookworm
LABEL authors="mike"

RUN set -eux; \
    apt update && \
    apt upgrade -y --no-install-recommends

COPY requirements.txt .
RUN pip install -r requirements.txt && \
    pip install debugpy

RUN mkdir -p /app

WORKDIR /app
COPY . .

CMD ["python", "-m", "main"]

# TAG: kweather-consumer