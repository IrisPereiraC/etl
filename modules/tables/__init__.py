import pandas as pd
from pyspark.sql import SparkSession

from modules.tables.TableLixo import TableLixo
from modules.tables.TableRegiao import TableRegiao
from modules.tables.TableTipoLixo import TableTipoLixo
from modules.tables.TableDistrito import TableDistrito

TABLES = (TableLixo, TableTipoLixo, TableRegiao, TableDistrito,)

def persist_tables(
        spk_cursor: SparkSession, db_url: str, db_properties: dict, treated_data_heap: dict[str, pd.DataFrame]
    ) -> None:
    print("Persistindo tabelas...")
    for i, table_class in enumerate(TABLES):
        print(f"\t[{i+1}/{len(TABLES)}] Tabela \"{table_class.table_name}\"...")

        table = table_class(spk_cursor, treated_data_heap)
        table.persist_table(db_url, db_properties)
    print("Gravação finalizada!")

