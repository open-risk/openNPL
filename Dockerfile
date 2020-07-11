FROM python:3.7-slim
MAINTAINER Open Risk <www.openriskmanagement.com>
LABEL maintainer="info@openrisk.eu"
EXPOSE 8080
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE openNPL.settings
RUN mkdir /opennpl
WORKDIR /opennpl
COPY requirements.txt /opennpl/
RUN pip install -r requirements.txt
COPY . /opennpl/
RUN python /opennpl/manage.py makemigrations
RUN python /opennpl/manage.py migrate
RUN python /opennpl/createadmin.py
RUN python /opennpl/manage.py collectstatic --no-input
RUN /opennpl/dockerfixtures.sh
