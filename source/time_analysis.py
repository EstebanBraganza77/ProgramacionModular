import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def time_evolution(dataframe: pd.DataFrame) -> None:
    """
    Plots the time evolution of permits, handguns, and long guns over the years.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data with 'year', 'permit',
    'handgun', and 'long_gun' columns.

    Returns:
    None
    """
    data_by_year = dataframe.groupby('year')[['permit', 'handgun', 'long_gun']].sum()
    plt.figure(figsize=(12, 6))

    sns.lineplot(x='year', y='permit', data=data_by_year, label='Permits')
    sns.lineplot(x='year', y='handgun', data=data_by_year, label='Hand Guns')
    sns.lineplot(x='year', y='long_gun', data=data_by_year, label='Long Guns')

    plt.title('Q 4.1 Evolution of guns and permits')
    plt.ylabel('Guns/permits counts')
    plt.legend(title='Category', loc='upper left')
    plt.show()


def comment_time_evolution_plot() -> None:
    """
    Comments the time evolution of permits, handguns, and long guns.
    """

    print(
        '''
        Q 4.2 Análisis de gráfico:\n
        
        De acuerdo con el gráfico que podemos observar tenemos una tendencia positiva en
        el número anual de armas de mano, armas largas y de permisos. Tenemos un aumento especialmente
        alto en el año 2016 de permisos de porte de armas en dónde se ve un cambio en la tendencia en la
        cual aumenta significativamente el número de permisos concedidos. También se puede apreciar el
        año 2020 en donde hay un declive significativo que coincide con la pandemia de COVID 19. 
        
        Por otro lado al analizar el el reportaje de CNN vemos que en el año 2017 tuvimos un pico
        de muertes por tiroteos masivos que parece coincidir con los años de mayor número de permisos 
        y de armas de mano.
        
        Vemos que alrededor del año 2014 el número de armas de mano supera a las armas largas coincidiendo
        con el aumento de los permisos. En los años anteriores el número de armas largas era superior al de
        armas de mano. Estos gráficos parecen sugerir una correlación entre la obtención de 
        permisos de porte de armas y el número de muertes ocasionadas por armas. Lo cual pordía ser un argumento
        en contra de la permisividad que existe en EEUU para portar armas de fuego.
        ''')
