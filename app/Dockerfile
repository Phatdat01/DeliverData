FROM python:3.9-slim-buster

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install openjdk-11-jdk -yqq

COPY requirements.txt /app/requirements.txt
RUN pip install --force-reinstall -r app/requirements.txt

COPY pyspark_app.py /app/pyspark_app.py

ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python

ENTRYPOINT ["spark-submit", "/app/pyspark_app.py"]

CMD ["spark-submit", "--master", "local[*]", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2", "pyspark_app.py"]
# CMD ["python", "demo.py"]



