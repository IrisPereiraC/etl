from pyspark.sql import DataFrame
from modules.tables.ITable import ITable
from modules.treated_files import EnumTreatedFiles


class TableDistrito(ITable):

    table_name = "distrito"

    def _transform_data(self) -> DataFrame:
        df_districs_pd = self.treated_data_heap[EnumTreatedFiles.DISTRICT.value]

        df_districs_pd = df_districs_pd.rename(columns={"nome": "bairro"})[["id", "bairro", "região"]]
        df_districs_pd["cidade"] = "São Paulo"

        df_regions_pd = df_districs_pd["região"].drop_duplicates().sort_values().reset_index(
            drop=True
        ).to_frame().rename_axis("regiao_id").reset_index()

        df_districs_spk = self.spk_cursor.createDataFrame(df_districs_pd.merge(df_regions_pd).drop(columns="região"))
        return df_districs_spk
