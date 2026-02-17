FROM python:3.11

WORKDIR /app

COPY pyproject.toml .
RUN pip install fastapi uvicorn pydantic[email]

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
