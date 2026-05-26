from pyspark.sql import DataFrame
from modules.tables.ITable import ITable
from modules.treated_files import EnumTreatedFiles


class TableRegiao(ITable):

    table_name = "regiao"

    def _transform_data(self) -> DataFrame:
        df_districs_pd = self.treated_data_heap[EnumTreatedFiles.DISTRICT.value]
        df_regions_pd = df_districs_pd["região"].drop_duplicates().rename(
            "nome"
        ).sort_values().to_frame().rename_axis("id").reset_index()

        df_regions_spk = self.spk_cursor.createDataFrame(df_regions_pd)
        return df_regions_spk
