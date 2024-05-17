import pandas as pd
import yake

class DataFrameEntity:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def drop_columns(self, columns):
        self.df.drop(columns, axis=1, inplace=True)

    def reset_index(self):
        self.df.reset_index(inplace=True)

    def set_index(self, index_column):
        self.df.set_index(index_column, inplace=True)

    def remove_row_by_index(self, index_value):
        self.df.drop(index_value, inplace=True)

    def split_coordinates_column(self, coordinates_column):
        self.df[['coord_X', 'coord_Y']] = self.df[coordinates_column].str.split(',', expand=True)

    def convert_to_float(self, columns):
        for column in columns:
            self.df[column] = pd.to_numeric(self.df[column])

    def display_info(self):
        print('DataFrame Info:')
        print(self.df.info())

class DataFrameBoundary:
    def __init__(self, filepath):
        self.controller = DataFrameControl(filepath)

    def get_reviews(self, column_name):
        if column_name in self.controller.dataframe_entity.df.columns:
            reviews_series = self.controller.dataframe_entity.df[column_name]
            return reviews_series.to_dict()
        else:
            raise ValueError(f"Столбца '{column_name}' нет в DataFrame.")

    def get_all_dataframe(self):
        if not self.controller.dataframe_entity.df.empty:
            print('Возвращаем весь DataFrame целиком:')
            return self.controller.dataframe_entity.df
        else:
            raise ValueError("The DataFrame пуст. Попробуйте снова")


    
class DataFrameControl:
    def __init__(self, filepath):
        self.dataframe_entity = DataFrameEntity(filepath)

    def process_data(self):
        columns_for_deletion = ['web-scraper-start-url','web-scraper-order','review_link-href', 'review_link']
        except_raion = 'АвтоТехСтрой'

        self.dataframe_entity.drop_columns(columns_for_deletion)
        self.dataframe_entity.set_index('title')
        self.dataframe_entity.remove_row_by_index(except_raion)
        self.dataframe_entity.reset_index()  # Столбец с названием жилого комплекса вернулся
        self.dataframe_entity.split_coordinates_column('coord')
        self.dataframe_entity.convert_to_float(['coord_X', 'coord_Y'])
        self.dataframe_entity.display_info()
