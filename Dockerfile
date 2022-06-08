FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN echo "{\"secret\" : \"$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')\"}" > /app/config.json
COPY . /app
CMD python manage.py runserver 0.0.0.0:8000