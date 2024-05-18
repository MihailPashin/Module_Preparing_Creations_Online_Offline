from dependency_injector import containers, providers
from Loading_DataSet.Pandas_ECB_df import DataFrameEntity,DataFrameBoundary,DataFrameControl


class Pandas_Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    dataframe_entity = providers.Factory(DataFrameEntity, filepath=config.filepath)
    dataframe_control = providers.Factory(DataFrameControl, dataframe_entity=dataframe_entity)
    dataframe_boundary = providers.Factory(DataFrameBoundary, control=dataframe_control)
