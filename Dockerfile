FROM python:3.6

WORKDIR /app

RUN pip install pipenv
ADD Pipfile ./
RUN pipenv install --skip-lock --deploy --system

COPY . ./
RUN python manage.py migrate
