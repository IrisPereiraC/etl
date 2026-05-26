from dotenv import load_dotenv
from modules import jdbc_setup
from modules.PySparkCursor import PySparkCursor

if __name__ == "__main__":
    print("ETL V 2.0")

    load_dotenv()
    jdbc_path = jdbc_setup.resolve_jdbc()
    db_url, db_properties = jdbc_setup.load_db_credentials()

    spk_cursor = PySparkCursor(jdbc_path)
    pass