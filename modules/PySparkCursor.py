from pyspark.sql import SparkSession

class PySparkCursor:

    client: SparkSession

    def __init__(self, jdbc_path: str) -> None:
        self.client = SparkSession.builder.appName("ETL TCC").config("spark.jars", jdbc_path).getOrCreate()