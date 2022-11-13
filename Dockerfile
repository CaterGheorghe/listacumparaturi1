FROM python:3.10.4-slim
FROM PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR  /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
