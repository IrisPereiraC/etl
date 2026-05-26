import pandas as pd
from pyspark.sql import DataFrame
from modules.tables.ITable import ITable


class TableTipoLixo(ITable):

    table_name = "tipo_lixo"

    def _transform_data(self) -> DataFrame:
        return self.spk_cursor.createDataFrame(pd.DataFrame([{
            "id": 1, "nome": "Entulho", "lixo_id": 1
        }]))
