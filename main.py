import os
from source.read_clean import read_clean, clean_csv, clean_col
from source.process import breakdown_date, erase_month
from source.group import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
from source.time_analysis import time_evolution, comment_time_evolution_plot
from source.state_analysis import (groupby_state, clean_states, merge_datasets,
                                   calculate_relative_values, outliers_analysis)
from source.maps import generate_map

path_guns = os.path.join('Data', 'nics-firearm-background-checks.csv')
path_us_state_populations = os.path.join('Data', 'us-state-populations.csv')
maps_path = './maps'
url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
geo_json_url = f"{url}/us-states.json"


def main():
    """
    Executes the data processing, analysis, and visualization pipeline.

    Reads and cleans firearm background check data and US state populations data.
    Performs data cleaning and preprocessing tasks.
    Analyzes data over time, printing analysis results for handguns and long guns.
    Generates time evolution plots and comments on the trends observed.
    Performs state-level analysis including data grouping, cleaning, merging, and calculating relative values.
    Detects outliers in the state-level analysis results.
    Generates choropleth maps showing relative values across US states for permit percentage,
    long gun percentage, and handgun percentage.

    Parameters:
    None

    Returns:
    None
    """

    data = read_clean(path_guns)
    populations_data = read_clean(path_us_state_populations)
    data = clean_csv(data)
    data = clean_col(data)
    data = breakdown_date(data)
    data = erase_month(data)
    group_data = groupby_state_and_year(data)
    print_biggest_handguns(group_data)
    print_biggest_longguns(group_data)
    time_evolution(data)
    comment_time_evolution_plot()
    group_state = groupby_state(group_data)
    group_state = clean_states(group_state)
    group_state = merge_datasets(group_state, populations_data)
    group_state = calculate_relative_values(group_state)
    outliers_analysis(group_state)
    for metric, color in [('permit_perc', 'RdBu'), ('longgun_perc', 'YlOrBr'), ('handgun_perc', 'PuBuGn')]:
        generate_map(save_path=maps_path, dataframe=group_state,
                     column_to_plot=metric, geo_json=geo_json_url, color=color)


if __name__ == '__main__':
    main()
