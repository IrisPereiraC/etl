import os

from pyspark.sql import SparkSession
from modules.tables.TableLixo import TableLixo
from modules.tables.TableTipoLixo import TableTipoLixo

TABLES = (TableLixo, TableTipoLixo,)

def persist_tables(spk_cursor: SparkSession, db_url: str, db_properties: dict):
    print("Persisitindo tabelas...")
    for i, table_class in enumerate(TABLES):
        print(f"\t[{i+1}/{len(TABLES)}] Tabela \"{table_class.table_name}\"...")

        table = table_class(spk_cursor)
        table.persist_table(db_url, db_properties)
    print("Gravação finalizada!")

