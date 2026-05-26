from pyspark.sql import DataFrame
from modules.tables.ITable import ITable
from modules.treated_files import EnumTreatedFiles


class TableRegiao(ITable):

    table_name = "regiao"

    def _transform_data(self) -> DataFrame:
        df_districs_pd = self.treated_data_heap[EnumTreatedFiles.DISTRICT.value]
        df_districs_pd = df_districs_pd["região"].rename("nome").to_frame().rename_axis("id").reset_index()

        df_districs_spk = self.spk_cursor.createDataFrame(df_districs_pd)
        return df_districs_spk
