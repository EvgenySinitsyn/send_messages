FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /send_message
ADD . /send_message
RUN pip install -r requirements.txt
