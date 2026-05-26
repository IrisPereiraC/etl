import pandas as pd
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType

from modules.tables.ITable import ITable

class TableLixo(ITable):

    table_name = "lixo"

    def __init__(self, spk_cursor: SparkSession):
        self.spk_cursor = spk_cursor

    def _transform_data(self) -> DataFrame:
        df = self.spk_cursor.createDataFrame(pd.DataFrame([{"id": 1}]))
        df = df.withColumn("peso", lit(None).cast(StringType()))
        return df
