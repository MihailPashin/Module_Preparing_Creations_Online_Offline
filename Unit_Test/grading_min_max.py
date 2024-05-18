import unittest
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sklearn.preprocessing import MinMaxScaler
from Containers.Normalize_Weigth import NormalizerWeight_Container

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.data_boundary = NormalizerWeight_Container().boundary()

    def test_process_grading(self):
        data = {
            'averall_ves': [5, 6, 7],
            'Положительная': [3, 4, 5],
            'Негативная': [1, 2, 3],
            'Нейтральная': [2, 3, 4],
            'Group': ['A', 'B', 'A']
        }
        df = pd.DataFrame(data)


        processed_df = self.data_boundary.process_grading(df)
        print(processed_df.info)

        expected_columns = ['averall_ves', 'Положительная', 'Негативная', 'Нейтральная', 'Group', 'svess']
        self.assertCountEqual(processed_df.columns, expected_columns)



if __name__ == '__main__':
    unittest.main()

