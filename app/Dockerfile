FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python3"]
CMD ["src/app.py"]