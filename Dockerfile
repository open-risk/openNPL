FROM python:3.9-slim
LABEL version="0.6"
LABEL author="Open Risk <www.openriskmanagement.com>"
LABEL description="openNPL: Open Source Credit Portfolio Management"
LABEL maintainer="info@openrisk.eu"
EXPOSE 8080
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE openNPL.settings
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]
RUN apt-get update && apt-get install -y \
    gdal-bin \
    proj-bin \
    libgdal-dev \
    libproj-dev \
    spatialite-bin\
    libsqlite3-mod-spatialite
RUN mkdir /opennpl
WORKDIR /opennpl
COPY requirements.txt /opennpl/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /opennpl/
RUN rm -f /opennpl/venv
RUN rm -f /opennpl/db.sqlite3
RUN rm -rf /opennpl/npl_portfolio/migrations/*
RUN rm -rf /opennpl/sflp_portfolio/migrations/*
RUN rm -rf /opennpl/start/migrations/*
RUN python /opennpl/manage.py makemigrations start
RUN python /opennpl/manage.py makemigrations npl_portfolio
RUN python /opennpl/manage.py makemigrations sflp_portfolio
RUN python /opennpl/manage.py migrate
RUN python /opennpl/createadmin.py
RUN python /opennpl/manage.py collectstatic --no-input
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]