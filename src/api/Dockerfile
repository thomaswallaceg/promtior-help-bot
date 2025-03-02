FROM python:3.11-slim

RUN pip install poetry==2.1.1

RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./README.md ./poetry.lock* ./

COPY ./package[s] ./packages

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./app ./app

RUN poetry install --no-interaction --no-ansi

EXPOSE 8080

ENV GROQ_API_KEY=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

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080
