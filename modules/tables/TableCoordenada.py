from pyspark.sql import DataFrame
from modules.tables.ITable import ITable
from modules.treated_files import EnumTreatedFiles


class TableCoordenada(ITable):

    table_name = "coordenada"

    def _transform_data(self) -> DataFrame:
        df_districs_pd = self.treated_data_heap[EnumTreatedFiles.DISTRICT.value]

        df_coords_pd = df_districs_pd.rename(columns={"id": "endereco_id", "lat": "latitude", "long": "longitude"})[[
            "latitude", "longitude", "endereco_id"
        ]]
        df_coords_pd = df_coords_pd.sort_values(
            ["latitude", "longitude"]
        ).reset_index(drop=True).rename_axis("id").reset_index()

        df_coords_spk = self.spk_cursor.createDataFrame(df_coords_pd)
        return df_coords_spk
