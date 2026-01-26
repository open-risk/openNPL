# Copyright (c) 2026 Open Risk (https://www.openriskmanagement.com)
FROM postgres:17-bookworm
LABEL version="0.6.4"
LABEL author="Open Risk <www.openriskmanagement.com>"
LABEL description="openNPL: Open Source Credit Portfolio Management"
LABEL maintainer="info@openriskmanagement.com"
EXPOSE 8080
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE openNPL.settings
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]
RUN apt-get update && apt-get install -y
RUN apt install postgresql postgresql-client -y
RUN apt install postgresql-plpython3-17 -y
RUN mkdir /opennpl
WORKDIR /opennpl
COPY requirements.txt /opennpl/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#
#COPY locale/ /opennpl/locale/
#COPY openNPL/ /opennpl/openNPL/
#COPY start/ /opennpl/start/
#COPY common/ /opennpl/common/
#COPY templates/ /opennpl/templates/
#COPY sflp_portfolio/ /opennpl/sflp_portfolio/
#COPY npl_portfolio/ /opennpl/npl_portfolio/
#COPY static/ /opennpl/static/
#
#COPY manage.py /opennpl/
#COPY createadmin.py /opennpl/
#
#RUN python /opennpl/manage.py makemigrations start
#RUN python /opennpl/manage.py makemigrations npl_portfolio
#RUN python /opennpl/manage.py makemigrations sflp_portfolio
#RUN python /opennpl/manage.py migrate
#RUN python /opennpl/createadmin.py
#RUN python /opennpl/manage.py collectstatic --no-input
#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]