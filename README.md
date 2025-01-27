# Solución de la PEC 4 

### Realizado por: Esteban Braganza

Este repositorio contiene mi solución para la PEC4 de la materia **Progamación para ciencia de datos**. El código está dividido de tal forma que cada pregunta está resuelta en un módulo diferente.
Cada pregunta se irá imprimiendo según la PEC lor requiera en la linea de comandos. Los comentarios solicitados en algunas de las preguntas también se imprimirán en la línea de comandos según se necesita. Este es un ejemplo de como se puede implementar un proyecto de programación completo, tomando en cuenta buenas prácticas y modulzarización, además se implementan algunas pruebas unitarias para asegurar la calidad y robustez del código.

## Estructura del proyecto

```plaintext
/ebraganza_PEC4
│
├── Data
│   ├── nics-firearm-background-checks.csv
│   └── us-state-populations.csv
│
├── source
│   ├── __init__.py
│   ├── read_clean.py
│   ├── process.py
│   ├── time_analysis.py
│   ├── state_analysis.py
│   ├── group.py
│   └── maps.py
│
├── maps
│   └── (Los mapas generados se guardarán aquí)
│
├── tests
│   ├── __init__.py
│   ├── test_pec4.py
│
├── main.py
├── run_tests.py
├── requirements.txt
├── README.md
└── LICENCE
```
### Carpetas

- **Data**: Carpeta para almacenar todos los archivos de datos requeridos para el proyecto.
  - `nics-firearm-background-checks.csv`: Datos de verificación de antecedentes de armas de fuego.
  - `us-state-populations.csv`: Datos de población de los estados de EE.UU.
- **source**: Carpeta para los módulos fuente del proyecto. Incluye un archivo `__init__.py` para reconocerlo como un paquete.
  - `read_clean.py`: Módulo para leer y limpiar datos pregunta 1.
  - `process.py`: Módulo para procesar datos pregunta 2.
  - `time_analysis.py`: Módulo para análisis de datos basados en el tiempo pregunta 3.
  - `group.py`: Módulo para agrupar datos pregunta 4.
  - `state_analysis.py`: Módulo para análisis de datos por estado pregunta 5.
  - `maps.py`: Módulo para funcionalidades relacionadas con mapas pregunta 6.
- **maps**: Carpeta para almacenar los archivos de mapas generados.
- **tests**: Carpeta para almacenar los archivos de pruebas unitarias. Incluye un archivo `__init__.py` para reconocerlo como un paquete.
  - `test_pec4.py`: Pruebas unitarias para las tres primeras preguntas de la `PEC4`.


### Archivos

- `main.py`: Archivo principal donde se ejecuta el código primario del proyecto.
- `requirements.txt`: Archivo para listar las dependencias del proyecto que se pueden instalar usando `pip`.
- `README.md`: Archivo de documentación que describe el proyecto, cómo instalarlo, usarlo, etc.
- `LICENCE`: Archivo que especifica la licencia del proyecto.
- `run_tests.py`: Archivo que crea y ejecuta las suites de los tests unitarios.

## Instalación

Para instalar el proyecto es necesario seguir los siguientes pasos.

```sh
1. git clone https://github.com/EstebanBraganza77/ebraganza_PEC4.git 
2. cd ./ebraganza_PEC4
3. pip install -r requirements.txt
```

## Uso

Para ejecutar el proyecto después de instalarlo es necesario ejecutar el comando descrito en este apartado. Mientras se ejecuta se irán imprimiendo en pantalla las respuestas a las preguntas que lo requieren. 

### Nota importante:
En la pregunta que genera el gráfico de evolución temporal aparecerá una ventana con el gráfico generado pero la ejecución se parará si no se cierra el mismo. Por favor cerrar esta ventana para continuar con las demás preguntas.

```sh
python main.py
```

Análogamente se puede ejecutar el siguiente comando para ejecutar los tests. 

```sh
python run_tests.py
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENCE para más detalles.

## Lógica del Código

El módulo `main.py` importará todas las funciones escritas de sus respectivos módulos y ejecuta la función **main** la cual ejecuta en orden el análisis solicitado en el enunciado de la PEC.
Ya que cada función está ligada al output de la anterior se tiene que ejecutar en el orden descrito en este módulo.

```python
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
```

Por otro lado el módulo `run_tests.py` genera las suites para probar las tres primeras preguntas de la PEC4 y este archivo ejecuta los tests implementados. 

```python
import unittest
from tests.test_pec4 import TestReadClean, TestProcess, TestGroup


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReadClean))
    suite.addTest(unittest.makeSuite(TestProcess))
    suite.addTest(unittest.makeSuite(TestGroup))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
```



