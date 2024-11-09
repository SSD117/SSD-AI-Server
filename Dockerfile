FROM python:alpine3.19 as builder

ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /app/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:alpine3.19

WORKDIR /app

ENV PATH="/app/venv/bin:$PATH"

COPY . .
COPY --from=builder /app/venv /app/venv

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

