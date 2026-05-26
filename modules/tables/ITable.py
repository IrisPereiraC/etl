from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame


class ITable(ABC):

    table_name: str
    spk_cursor: SparkSession

    def __init__(self, spk_cursor: SparkSession):
        if self.table_name is None:
            raise ValueError("Defina \"table_name\" ao definir classes filhas de \"ITable\"")
        self.spk_cursor = spk_cursor

    def persist_table(self, db_url: str, db_properties: dict):
        df = self._transform_data()
        self._write_to_db(df, db_url, db_properties)

    @abstractmethod
    def _transform_data(self) -> DataFrame:
        pass

    def _write_to_db(self, df: DataFrame, db_url: str, db_properties: dict):
        df.write.jdbc(db_url, self.table_name, properties=db_properties, mode="append")
