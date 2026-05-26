from pyspark.sql import SparkSession

def generate_cursor(jdbc_path: str) -> SparkSession:
    return SparkSession.builder.appName("ETL TCC").config("spark.jars", jdbc_path).getOrCreate()