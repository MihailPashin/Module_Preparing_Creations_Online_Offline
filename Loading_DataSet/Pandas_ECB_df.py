import pandas as pd
import yake
from Exception.user_exception import Varierty_of_Errors  # Ensure the correct spelling of the exception

class DataFrameEntity:
    def __init__(self, filename):
        self.df = pd.read_csv(filename, index_col=0)

    def drop_columns(self, columns):
        self.df.drop(columns, axis=1, inplace=True)

    def reset_index(self):
        self.df.reset_index(drop=True, inplace=True)

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
        print(self.df.info())

class DataFrameBoundary:
    def __init__(self, dataframe_entity):
        self.dataframe_entity = dataframe_entity

    def load_dataframe(self, filepath):
        return DataFrameEntity(filepath)

    def get_reviews(self, column_name):
        if column_name in self.dataframe_entity.df.columns:
            reviews_series = self.dataframe_entity.df[column_name].dropna()
            # Первые две строки из словаря
            for index, review in list(reviews_series.items())[:2]:
                print(f"Индекс: {index}, Отзыв: {review}")
                
            return reviews_series.to_dict()
        else:
            raise Varierty_of_Errors(f"Столбец '{column_name}' не найден в DataFrame.")

class DataFrameControl:
    def __init__(self, dataframe_entity):
        self.dataframe_entity = dataframe_entity

    def process_data(self):
        columns_for_deletion = ['web-scraper-start-url', 'review_link-href', 'review_link']
        except_raion = 'АвтоТехСтрой'

        self.dataframe_entity.drop_columns(columns_for_deletion)
        self.dataframe_entity.reset_index()
        self.dataframe_entity.set_index('title')
        self.dataframe_entity.remove_row_by_index(except_raion)
        self.dataframe_entity.reset_index()
        self.dataframe_entity.split_coordinates_column('coord')
        self.dataframe_entity.convert_to_float(['coord_X', 'coord_Y'])
        self.dataframe_entity.display_info()
