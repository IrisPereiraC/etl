from enum import StrEnum
import pandas as pd
from modules.Boto3Cursor import Boto3Cursor


class EnumTreatedFiles(StrEnum):

    DISTRICT = "trusted_district"
    LITTER = "trusted_litter"
    CLIMATE = "trusted_climate"

def load_treated_files(boto_cursor: Boto3Cursor) -> dict[str, pd.DataFrame]:
    data_heap = {}
    print("Carregando dados tratados do S3...")
    for i, item in enumerate(EnumTreatedFiles):
        filename = item.value
        print(f"\t[{i+1}/{len(EnumTreatedFiles)}] {filename}...")
        data_heap[filename] = boto_cursor.ler(f"{filename}.csv")
    print("Feito!")
    return data_heap