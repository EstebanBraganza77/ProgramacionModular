""" This module implements tests for the PEC4 functions"""

import unittest
import pandas as pd
import os
from source.read_clean import read_clean, clean_csv, clean_col
from source.process import breakdown_date, erase_month


class TestReadClean(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Define paths to data files
        cls.path_guns = os.path.join('Data', 'nics-firearm-background-checks.csv')

    def test_read_clean(self):
        # Test read_clean function with real CSV file
        df = read_clean(self.path_guns)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 27)

    def test_clean_csv(self):
        # Test clean_csv function with real CSV file
        df = read_clean(self.path_guns)
        cleaned_df = clean_csv(df)
        self.assertEqual(list(cleaned_df.columns), ['month', 'state', 'permit', 'handgun', 'long_gun'])
        self.assertEqual(len(cleaned_df), len(df))

    def test_clean_col(self):
        # Test clean_col function with real CSV file
        df = pd.read_csv(self.path_guns)
        cleaned_df = clean_col(df)
        self.assertIn('long_gun', cleaned_df.columns)
        self.assertNotIn('longgun', cleaned_df.columns)


class TestProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Define paths to data files
        cls.data = read_clean(os.path.join('Data', 'nics-firearm-background-checks.csv'))
        cls.clean_data = clean_csv(cls.data)
        cls.clean_data = clean_col(cls.clean_data)

    def test_breakdown_date(self):
        test_data = breakdown_date(self.clean_data)
        self.assertIsInstance(test_data, pd.DataFrame)
        self.assertIn('year', list(test_data.columns))
        self.assertIn('month', list(test_data.columns))

    def test_erase_month(self):
        test_data = breakdown_date(self.clean_data)
        test_data = erase_month(test_data)
        self.assertIsInstance(test_data, pd.DataFrame)
        self.assertNotIn('month', list(test_data.columns))


if __name__ == '__main__':
    unittest.main()
