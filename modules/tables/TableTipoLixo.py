import pandas as pd
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from modules.tables.ITable import ITable


class TableTipoLixo(ITable):

    table_name = "tipo_lixo"

    def __init__(self, spk_cursor: SparkSession):
        self.spk_cursor = spk_cursor

    def _transform_data(self) -> DataFrame:
        return self.spk_cursor.createDataFrame(pd.DataFrame([{
            "id": 1, "nome": "Entulho", "lixo_id": 1
        }]))
