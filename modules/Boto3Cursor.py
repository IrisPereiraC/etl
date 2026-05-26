import os
from io import BytesIO, StringIO
import boto3
import pandas as pd
from botocore.client import BaseClient

class Boto3Cursor:

    cursor: BaseClient
    bucket_name: str

    def __init__(self):
        bucket_name_env = os.getenv("S3_BUCKET")
        if bucket_name_env is None :
            raise EnvironmentError("Defina a variável de .env do BUCKET")

        self.bucket_name = bucket_name_env
        self.cursor = boto3.client("s3")

    def ler(self, file_key: str) -> pd.DataFrame:
        res = self.cursor.get_object(Bucket=self.bucket_name, Key=file_key)
        code = res["ResponseMetadata"]["HTTPStatusCode"]
        if code != 200:
            raise FileNotFoundError(f"Não foi possível encontrar \'{file_key}\' no S3...")

        found_bytes = res["Body"].read()
        return pd.read_csv(BytesIO(found_bytes))

    def gravar(self, file_key: str, df: pd.DataFrame):
        raise NotImplementedError()
        # csv_buffer = StringIO()
        # df.to_csv(csv_buffer, index=False, sep="|")
        # self.cursor.put_object(
        #     Bucket=self.target_bucket_name, Key=f"{file_key}.csv", Body=csv_buffer.getvalue()
        # )
