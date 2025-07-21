FROM python:3.12-slim

WORKDIR /app

COPY debug.py .

RUN pip install kafka-python

CMD ["python", "debug.py"]
