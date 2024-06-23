"""
This module provides functions for processing a DataFrame containing firearm permit data.

Functions:
- erase_month(dataframe: pd.DataFrame) -> pd.DataFrame: Removes the 'month' column from the DataFrame.
- breakdown_date(dataframe: pd.DataFrame) -> pd.DataFrame: Breaks down the 'month' column into separate 'year' and 'month' columns.
"""

import pandas as pd


def erase_month(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Removes 'month' column from the DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing 'month' column.

    Returns:
    pd.DataFrame: The DataFrame without 'month' column.
    """
    dataframe = dataframe.drop(columns=['month'])
    print('Q 2.2', dataframe.columns.tolist())
    print(dataframe.head())
    return dataframe


def breakdown_date(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Breaks down the 'month' column into separate 'year' and 'month' columns.

    Parameters:
    dataframe (pd.DataFrame): The original DataFrame with a 'month' column.

    Returns:
    pd.DataFrame: A new DataFrame with additional 'year' and 'month' columns.
    """
    processed_df = (
        dataframe
        .copy()
        .assign(
            year=lambda df_: df_.month.apply(lambda date: int(str(date).split('-')[0])),
            month=lambda df_: df_.month.apply(lambda date: int(str(date).split('-')[1]))
        )
    )
    print('Q 2.1', processed_df.head())
    return processed_df
