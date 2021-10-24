FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk update --no-cache
RUN apk add --no-cache gcc
RUN apk add --no-cache musl-dev linux-headers
RUN apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
