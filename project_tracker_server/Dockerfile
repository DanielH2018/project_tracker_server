FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /server
WORKDIR /server/

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin python3-gdal
RUN pip install -r requirements.txt
