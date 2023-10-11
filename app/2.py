from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Kafka to PySpark") \
    .getOrCreate()

# Configure Kafka connection properties
kafka_bootstrap_servers = "localhost:9092"
kafka_topic = "your_topic"
kafka_group_id = "your_group_id"

# Read data from Kafka topic
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "earliest") \
    .option("group.id", kafka_group_id) \
    .load()

# Extract key and value columns from Kafka data
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Perform some operations on the received data
processed_df = df.withColumn("upper_value", upper(col("value")))

# Start the streaming query
query = processed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()