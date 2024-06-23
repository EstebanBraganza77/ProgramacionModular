"""
This module provides functionality to generate a choropleth map based on a given DataFrame and save it as an image.
The map is generated using Folium and saved as a PNG file using PIL.
"""


import io
import folium
from PIL import Image
import pandas as pd
from folium import Map


def generate_map(save_path: str, dataframe: pd.DataFrame, column_to_plot: str, geo_json: str, color: str) -> None:
    """
    Generates a choropleth map based on the provided DataFrame and saves it as a PNG image.

    Parameters:
    save_path (str): The directory path where the generated map image will be saved.
    dataframe (pd.DataFrame): The DataFrame containing the data to be plotted on the map.
    column_to_plot (str): The column name in the DataFrame that contains the data to be visualized on the map.
    geo_json (str): The path to the GeoJSON file that contains the geographical boundaries for the map.
    color (str): The color scheme to use for the choropleth map.

    Returns:
    None
    """
    us_map: Map = folium.Map(location=[40, -95], zoom_start=4)
    folium.Choropleth(
        geo_data=geo_json,
        name="choropleth",
        data=dataframe,
        columns=["code", column_to_plot],
        key_on="feature.id",
        fill_color=color,
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=column_to_plot
    ).add_to(us_map)

    folium.LayerControl().add_to(us_map)

    img_data = us_map._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(f'{save_path}/{column_to_plot}.png')
