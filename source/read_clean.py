"""
This module provides functions for reading, cleaning, and transforming a CSV file containing
firearm permit data.

Functions:
- read_clean(path: str) -> pd.DataFrame: Reads a CSV file and returns a DataFrame.
- clean_csv(dataframe: pd.DataFrame) -> pd.DataFrame: Cleans the DataFrame by selecting specific columns.
- clean_col(dataframe: pd.DataFrame) -> pd.DataFrame: Cleans the column names of the DataFrame.
"""

import pandas as pd


def read_clean(path: str) -> pd.DataFrame:
    """
    Reads a CSV file from the specified path and returns a DataFrame.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the CSV data.
    """
    return pd.read_csv(path, sep=',')


def clean_csv(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by selecting specific columns and returning a copy of it.

    Parameters:
    dataframe (pd.DataFrame): The original DataFrame to be cleaned.

    Returns:
    pd.DataFrame: A new DataFrame containing only the specified columns.
    """
    clean_df = dataframe.loc[:, ['month', 'state', 'permit', 'handgun', 'long_gun']].copy()
    print('Q 1.2:', list(clean_df.columns))
    return clean_df


def clean_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the column names of the DataFrame by renaming 'longgun' to 'long_gun' if it exists.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame with columns to be cleaned.

    Returns:
    pd.DataFrame: The DataFrame with cleaned column names.
    """
    print('Q 1.3', list(dataframe.columns))
    if 'longgun' in dataframe.columns:
        dataframe.rename({'longgun': 'long_gun'}, axis=1, inplace=True)
    return dataframe
