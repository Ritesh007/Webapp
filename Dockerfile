FROM centos:centos6

MAINTAINER ritesh@kuchukulla.com

RUN yum install -y flask

COPY . /src

EXPOSE 8080

CMD cd /src && python ./Webapplication/Webapplication/webapp.py