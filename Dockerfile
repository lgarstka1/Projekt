FROM python:3.10-slim AS builder
WORKDIR /app


RUN apt-get update && apt-get install -y gcc libpq-dev


COPY app/requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM builder AS test


RUN pip install --no-cache /app/wheels/*


COPY app/src/ /app/src/
COPY app/tests/ /app/tests/


RUN python -m pytest /app/tests/

FROM python:3.10-slim AS final

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

COPY app/src/ /app/src/

CMD ["python", "src/app.py"]