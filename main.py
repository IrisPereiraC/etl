from dotenv import load_dotenv
from modules import jdbc_setup, pyspark_factory, tables

if __name__ == "__main__":
    print("ETL V 2.2\n")

    load_dotenv()
    jdbc_path = jdbc_setup.resolve_jdbc()
    db_url, db_properties = jdbc_setup.load_db_credentials()

    spk_cursor = pyspark_factory.generate_cursor(jdbc_path)

    tables.persist_tables(spk_cursor, db_url, db_properties)
