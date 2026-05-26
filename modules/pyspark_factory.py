from pyspark.sql import SparkSession

def generate_cursor(jdbc_path: str) -> SparkSession:
    print("Carregando cursor do Spark...")
    cursor = SparkSession.builder.appName("ETL TCC").config("spark.jars", jdbc_path).getOrCreate()
    cursor.sparkContext.setLogLevel("ERROR")
    print("Liberado!\n")
    return cursor