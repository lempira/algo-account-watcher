FROM python:3.12.3-slim-bookworm

# Create the app user so that the app does not run as root
RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

RUN apt-get update
RUN apt-get install -y pipx && pipx ensurepath
RUN pipx install poetry
ENV PATH="/$HOME/.local/bin:$PATH"

COPY . .

RUN chown -R app:app $APP_HOME
USER app

RUN poetry install --no-dev

ENV PORT 80
# CMD poetry run gunicorn --bind 0.0.0.0:$PORT api.main:app -k uvicorn.workers.UvicornWorker
CMD poetry run uvicorn api.main:app --host 0.0.0.0 --port ${PORT} --workers 1
