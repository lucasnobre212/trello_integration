# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY . ./trello_integration
WORKDIR ./trello_integration

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV TRELLO_API_KEY=6b3d410a9c4c1914c803dd64a8b77221

RUN pip3 install -r requirements.txt

EXPOSE 7000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
