from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('my_app')\
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1')\
    .getOrCreate()

reviewdf = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .load()
        # .option("subscribe", "delta-pipeline") \
        # .option("startingOffsets", "latest") \
print(reviewdf)