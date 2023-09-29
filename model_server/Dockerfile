FROM python:3.9-slim-buster


RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install openjdk-11-jdk -yqq

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

RUN pip install pyspark==3.3.2

ENV PORT 5000
