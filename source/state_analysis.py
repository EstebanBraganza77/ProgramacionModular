"""
This module contains functions for processing and analyzing state data.
The functions include operations for grouping by state, cleaning state data,
merging datasets, calculating relative values, and analyzing outliers.
"""

import pandas as pd


def groupby_state(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Group the DataFrame by state and sum the values, removing the 'year' column.

    Args:
        dataframe (pd.DataFrame): The input DataFrame containing state data.

    Returns:
        pd.DataFrame: The grouped DataFrame with summed values for each state.
    """
    dataframe = dataframe.groupby('state').sum().reset_index().drop('year', axis=1)
    print('Q 5.1', dataframe.head())
    return dataframe


def clean_states(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove specified territories from the DataFrame and print the number of remaining states.

    Args:
        dataframe (pd.DataFrame): The input DataFrame containing state data.

    Returns:
        pd.DataFrame: The cleaned DataFrame with specified territories removed.
    """
    states_to_erase = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    clean_dataframe = dataframe[~dataframe.state.isin(states_to_erase)]
    print('Q 5.2 The number of remaining states is:', clean_dataframe.state.nunique())
    return clean_dataframe


def merge_datasets(states_dataframe: pd.DataFrame, populations_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Merge the states DataFrame with the populations DataFrame on the 'state' column.

    Args:
        states_dataframe (pd.DataFrame): The DataFrame containing state data.
        populations_dataframe (pd.DataFrame): The DataFrame containing population data.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    merged_dataset = states_dataframe.merge(populations_dataframe, on='state', how='left')
    print('Q 5.3 Merged dataset:\n', merged_dataset.head())
    return merged_dataset


def calculate_relative_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate relative values (percentages) for permit, long gun, and handgun columns.

    Args:
        dataframe (pd.DataFrame): The input DataFrame containing state and population data.

    Returns:
        pd.DataFrame: The DataFrame with new calculated columns for percentages.
    """
    new_dataframe = (
        dataframe
        .assign(
            permit_perc=lambda df_: (df_.permit * 100) / df_.pop_2014,
            longgun_perc=lambda df_: (df_.long_gun * 100) / df_.pop_2014,
            handgun_perc=lambda df_: (df_.handgun * 100) / df_.pop_2014
        )
    )
    print('Q 5.4 New calculations:\n', new_dataframe.head())
    return new_dataframe


def outliers_analysis(dataframe: pd.DataFrame) -> None:
    """
    Analyze and handle outliers in the 'permit_perc' column, specifically for Kentucky.

    Args:
        dataframe (pd.DataFrame): The input DataFrame containing state data.

    Returns:
        None
    """
    total_mean = dataframe.permit_perc.mean()
    print(f'Q5.5.1 The average permit_perc value is: {round(total_mean, 2)}')
    print(f'Q5.5.2 Permit perc for Kentucky: {round(dataframe[dataframe.state == "Kentucky"].permit_perc.to_list()[0], 
                                                    2)}')
    dataframe.loc[dataframe.state == 'Kentucky', 'permit_perc'] = total_mean
    print(f'Q5.5.4 Average after change: {round(dataframe.permit_perc.mean(), 2)}')
    print(
        '''
        Q5.5.5\n 
        El valor ha cambiado significativamente pasando de 34.88 a 21.12 esto 
        se debe a que un valor atípico afecta de forma significativa a una medida de tendencia central 
        desplazándola de donde realmente se concentran los datos, esto puede afectar a muchos procesos
        principalmente si queremos realizar predicciones precisas o si realizamos cálculos de distancia 
        entre observaciones.
        ''')
