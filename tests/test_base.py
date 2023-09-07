from hugohu_pandas_package.base import NAME, pd

import unittest
from unittest.mock import patch
from hugohu_pandas_package.cli import filter_data


def test_base():
    assert NAME == "hugohu_pandas_package"


class TestFilterData(unittest.TestCase):

    @patch('hugohu_pandas_package.cli.pd.read_csv')
    def test_filter_data(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
            'Age': [25, 30, 35, 28, 32, 40]
        })

        filtered_df = filter_data('data/data.csv')

        # Add your assertions here
        self.assertEqual(len(filtered_df), 3)
        self.assertEqual(filtered_df['Name'].iloc[0], 'Charlie')