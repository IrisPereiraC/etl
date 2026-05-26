from pyspark.sql import SparkSession
from modules.tables.TableLixo import TableLixo
from modules.tables.TableTipoLixo import TableTipoLixo

TABLES = (TableLixo, TableTipoLixo,)

def persist_tables(spk_cursor: SparkSession, db_url: str, db_properties: dict):
    for table_class in TABLES:
        table = table_class(spk_cursor)
        table.persist_table(db_url, db_properties)

