FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN key=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
RUN echo    "{" \
            "\"secret\" : \"${key}\""    \
            "}" > /app/config.json

CMD python manage.py runserver 0.0.0.0:8000