from dotenv import load_dotenv
from modules import jdbc_setup, pyspark_factory, tables, treated_files
from modules.Boto3Cursor import Boto3Cursor

if __name__ == "__main__":
    print("ETL V 2.5\n")

    load_dotenv()
    jdbc_path = jdbc_setup.resolve_jdbc()
    db_url, db_properties = jdbc_setup.load_db_credentials()

    boto_cursor = Boto3Cursor()
    treated_data_heap = treated_files.load_treated_files(boto_cursor)

    spk_cursor = pyspark_factory.generate_cursor(jdbc_path)
    tables.persist_tables(spk_cursor, db_url, db_properties, treated_data_heap)
