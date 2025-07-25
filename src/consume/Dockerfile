FROM python:3.11-bookworm
LABEL authors="mike"


ENV TO_ADDR="8136036583@msg.fi.google.com"
ENV GMAIL_USER="michael.schmidt82@gmail.com"
ENV GMAIL_APP_PASS="vfvh tbco wdpl vyha"

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