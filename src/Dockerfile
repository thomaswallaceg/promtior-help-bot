FROM python:3.11-slim

RUN pip install poetry==2.1.1

WORKDIR /code

COPY ./pyproject.toml ./README.md ./poetry.lock* ./

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./app ./app

RUN poetry install --no-interaction --no-ansi
ENV GIT_PYTHON_REFRESH=quiet

COPY start.sh /code/
RUN chmod +x /code/start.sh

EXPOSE 8080
EXPOSE 8081
EXPOSE 11434

ENTRYPOINT ["/code/start.sh"]
