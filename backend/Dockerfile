FROM python:3.8-slim

RUN pip install --upgrade pip 

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /app 

WORKDIR /app 

COPY ./entrypoint.sh . 

ENTRYPOINT [ "sh","/app/entrypoint.sh" ]