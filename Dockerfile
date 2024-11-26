FROM python:3.11-slim as builder

# 가상환경 PATH 설정
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

# 필수 빌드 도구 및 라이브러리 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    build-essential \
    gfortran \
    libffi-dev \
    liblapack-dev \
    libopenblas-dev && \
    python -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# 의존성 설치
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

# 가상환경 PATH 설정
ENV PATH="/app/venv/bin:$PATH"

COPY . .
COPY --from=builder /app/venv /app/venv

# FastAPI 앱 실행
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
