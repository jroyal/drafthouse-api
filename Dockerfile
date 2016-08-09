from iron/python:2.7.11-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python server.py