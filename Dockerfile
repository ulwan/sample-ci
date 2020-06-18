FROM python:3.6-alpine

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]