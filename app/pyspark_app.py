from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PySpark Kafka MongoDB MySQL Example") \
    .getOrCreate()

# Define the schema for the Kafka message
schema = StructType().add("id", IntegerType()).add("name", StringType())

# Read Kafka events
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "9092:9092") \
    .option("subscribe", "my_topic") \
    .load()

# Parse the Kafka message as JSON
parsed_df = kafka_df.select(from_json(kafka_df.value.cast("string"), schema).alias("data"))
parsed_df = parsed_df.select("data.*")

# Read data from MongoDB
mongo_df = spark \
    .read \
    .format("mongo") \
    .option("spark.mongodb.input.uri", "mongodb://mongodb/demoMongo_db.collection") \
    .load()

# Perform transformations on the data
transformed_df = parsed_df.join(mongo_df, "id")

# Write the transformed data to MySQL
transformed_df.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://mysql:3306/demoMySQL_db") \
    .option("dbtable", "my_table") \
    .option("user", "username") \
    .option("password", "password") \
    .mode("append") \
    .save()

# Start the streaming query
query = transformed_df.writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

# Wait for the query to terminate
query.awaitTermination()