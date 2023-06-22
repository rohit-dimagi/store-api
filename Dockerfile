FROM python:3.11.1-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

workdir /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]