"""
This module provides functions for processing and analyzing a DataFrame containing firearm permit data.

Functions:
- groupby_state_and_year(dataframe: pd.DataFrame) -> pd.DataFrame: Groups the DataFrame by 'state' and 'year' columns and sums the values.
- print_biggest_handguns(dataframe: pd.DataFrame) -> None: Prints the state and year with the maximum number of 'handgun' values.
- print_biggest_longguns(dataframe: pd.DataFrame) -> None: Prints the state and year with the maximum number of 'long_guns' values.
"""


import pandas as pd


def groupby_state_and_year(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
      Groups the DataFrame by 'state' and 'year' columns and sums the values.

      Parameters:
      dataframe (pd.DataFrame): The DataFrame to be grouped.

      Returns:
      pd.DataFrame: The grouped DataFrame with summed values.
    """
    return dataframe.groupby(['state', 'year']).sum().reset_index()


def print_biggest_handguns(dataframe: pd.DataFrame) -> None:
    """
    Prints the state and year with the maximum number of 'handgun' values.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the grouped data.
    """
    max_idx = dataframe.handgun.argmax()
    print(f'Q 3.2  {dataframe.state[max_idx]} had the highest number of handguns in the year {dataframe.year[max_idx]}.')


def print_biggest_longguns(dataframe: pd.DataFrame) -> None:
    """
    Prints the state and year with the maximum number of 'long_guns' values.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the grouped data.
    """
    max_idx = dataframe.long_gun.argmax()
    print(f'Q 3.3  {dataframe.state[max_idx]} had the highest number of long guns in the year {dataframe.year[max_idx]}.')
