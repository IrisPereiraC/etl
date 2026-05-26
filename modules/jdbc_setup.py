import io
import os
import tarfile
from requests import get

LOCAL_PATH = "cache"
FILENAME = "jdbc.jar"
REMOTE_JDBC_URL = "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-9.7.0.tar.gz"

def load_db_credentials():
    url_env = os.environ.get("DB_URL")
    db_name_env = os.environ.get("DB_NAME")
    user_env = os.environ.get("DB_USER")
    passw_env = os.environ.get("DB_PASSWORD")
    if url_env is None or db_name_env is None or user_env is None or passw_env is None:
        raise EnvironmentError("Defina as variáveis de ambiente de banco de dados.")

    url = f"jdbc:mysql://{url_env}/{db_name_env}"
    properties = {"user": user_env, "password": passw_env, "driver": "com.mysql.cj.jdbc.Driver"}
    return url, properties

def resolve_jdbc() -> str:
    if not os.path.exists(LOCAL_PATH):
        os.mkdir(LOCAL_PATH)

    full_path = os.path.join(LOCAL_PATH, FILENAME)
    if not _check_for_jdbc(full_path):
        _get_jdbc(full_path)
    return full_path

def _check_for_jdbc(full_path) -> bool:
    return os.path.exists(full_path) & os.path.isfile(full_path)

def _get_jdbc(full_path):
    req = get(REMOTE_JDBC_URL)
    req.raise_for_status()

    content_stream = io.BytesIO(req.content)
    tar_content = tarfile.open(fileobj=content_stream)
    target_file = next(filter(lambda m: m.name.endswith(".jar"), tar_content.getmembers())).name
    bytes_content = tar_content.extractfile(target_file).read()
    open(full_path, "wb").write(bytes_content)
