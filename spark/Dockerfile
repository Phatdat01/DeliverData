FROM openjdk:11 AS java-installation

RUN apt-get update && apt-get install -y openjdk-11-jre
ENV JAVA_HOME /usr/local/openjdk-11

FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
RUN pip install --force-reinstall -r app/requirements.txt

COPY demo.py /app/demo.py

ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python

ENTRYPOINT ["pyspark"]

CMD ["spark-submit", "demo.py"]
# CMD ["python", "demo.py"]



