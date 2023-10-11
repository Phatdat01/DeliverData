from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
scala_version = '2.12'
spark_version = '3.2.1'

packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    'org.apache.kafka:kafka-clients:3.2.3'
]


spark = SparkSession.builder\
   .master("spark://spark-master:7077")\
   .appName("kafka-example")\
   .config("spark.jars.packages", ",".join(packages))\
   .getOrCreate()
