# Set base image
FROM python:3

# send stdout and stderr results directly to terminal 
# and does not store data in the buffer
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
