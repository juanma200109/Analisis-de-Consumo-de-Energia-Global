import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import ipywidgets as widgets
from ipywidgets import interact, fixed, interactive, VBox, HBox

# ==============================================================================
# Funcióin para crear histogramas
# ==============================================================================

def crear_histograma(data, nombre_col, etiqueta_eje_x, etiqueta_eje_y):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - nombre_col: Nombre de la columna que se va a graficar.
        - etiqueta_eje_x: Es la etiqueta del eje x.
        - etiqueta_eje_y: Es la etiqueta del eje y.
    salida: 
        - Un gráfico con un histograma.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de nombre_col.
        - El gráfico también se muestra en pantalla.
    """
    plt.hist(data[nombre_col], bins=24, alpha=0.5, color='blue', edgecolor='black')
    plt.xlabel(etiqueta_eje_x)
    plt.ylabel(etiqueta_eje_y)
    plt.title('Histograma de ' + nombre_col)
    
    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Histograma_" + nombre_col.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)
    plt.show()

# ==============================================================================
# Función para crear un grafico KDE (similar a la función de densidad de probabilidad)
# ==============================================================================

def crear_grafico_kde(data, nombre_col, etiqueta_eje_x, etiqueta_eje_y):
    """
    Entradas: 
        - data: Es la información que se va a graficar (dataframe).
        - nombre_col: Nombre de la columna que se va a graficar.
        - etiqueta_eje_x: Es la etiqueta del eje x.
        - etiqueta_eje_y: Es la etiqueta del eje y.
    Salida: 
        - Un gráfico con un grafico KDE.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de nombre_col.
        - El gráfico también se muestra en pantalla.
    """
    sns.kdeplot(data[nombre_col], fill=True, color='skyblue')
    plt.title('Grafico KDE de ' + nombre_col)
    plt.xlabel(etiqueta_eje_x)
    plt.ylabel(etiqueta_eje_y)

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "KDE_" + nombre_col.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)
    plt.show()

# ==============================================================================
# Bloxplot
# ==============================================================================
def crear_boxplot(data, nombre_col1, nombre_col2, titulo, etiqueta_eje_x, etiqueta_eje_y):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - nombre_col1: Nombre de la columna del DataFrame que se utilizará para el eje x (variable categórica para los boxplots).
        - nombre_col2: Nombre de la columna del DataFrame que se utilizará para el eje y (variable numérica cuyos valores se distribuirán en los boxplots).
        - titulo: Título del gráfico (string).
        - etiqueta_eje_x: Etiqueta para el eje x del gráfico (string).
        - etiqueta_eje_y: Etiqueta para el eje y del gráfico (string).

    Salida:
        - Un gráfico de boxplot que muestra la distribución de la variable numérica
          (nombre_col2) para cada categoría de la variable categórica (nombre_col1).
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """
    sns.boxplot(x = data[nombre_col1], y = data[nombre_col2], hue = data[nombre_col1], palette='viridis')
    plt.title(titulo, fontsize=16)
    plt.xlabel(etiqueta_eje_x, fontsize=12)
    plt.ylabel(etiqueta_eje_y, fontsize=12)

    # Estética extra
    sns.despine(offset=10, trim=True)  # Quitar bordes innecesarios
    plt.tight_layout()                 # Evita recortes de texto
    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Box_plot_" + nombre_col2.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)
    plt.show()

# ==============================================================================
# Grafico de líneas (multiples)
# ==============================================================================
def crear_graf_lineas(data, col_car1, col_car2, col_data, etiqueta_eje_x, etiqueta_eje_y, titulo):
    """
    Entradas:
        - data: Es un dataframe que contiene los datos de interes.
        - col_car1: Nombre de la columna caracteristica (por ejemplo: 'Country')
        - col_car2: Nombre de la columna caracteristica (por ejemplo: 'Year')
        - col_data: Nombre de la columna de los valores a graficar (por ejemplo: 'Renewable Energy Share (%)').
    Salidas:
        - Grafico de líneas que muestra el comportamiento promedio de las variables.
    """
    df_ordenado = data.sort_values(by=[col_car1, col_car2])

    # Obteniendo la lista única de países
    lista_paises = df_ordenado[col_car1].unique().tolist()

    # Agrupando por país y año y calculando la media (esto ya lo tenías bien)
    df_agrupado = df_ordenado.groupby([col_car1, col_car2]).mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 8))

    for pais in lista_paises:
        # Filtrando los datos para el país actual
        pais_data = df_agrupado[df_agrupado[col_car1] == pais]

        # Graficando la serie de tiempo para el país
        ax.plot(pais_data[col_car2], pais_data[col_data], label=pais)

    ax.set_xlabel(etiqueta_eje_x, fontsize=12)
    ax.set_ylabel(etiqueta_eje_y, fontsize=12)
    ax.set_title(titulo, fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Añadir leyenda en una ubicación óptima
    ax.legend(loc='best', fontsize=10)

    # Ajustar los márgenes
    plt.tight_layout()

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_lineas_" + col_data.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)
    # Mostrar el gráfico
    plt.show()

# ==============================================================================
# Grafico de correlación
# ==============================================================================

def crear_grafico_correlacion(data, cols, agrupar_por, titulo):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - cols: Lista de columnas que se van a graficar (dataframe).
        - titulo: Título del gráfico (string).

    Salida:
        - Un gráfico de correlación que muestra la relación entre las dos variables.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """
    # Ordenando el dataframe por país y luego por año
    df_ordenado = data.sort_values(by=[agrupar_por])

    # Obteniendo la lista única de países
    lista_paises = df_ordenado[agrupar_por].unique().tolist()

    # Agrupando por país y año y calculando la media (esto ya lo tenías bien)
    df_agrupado = df_ordenado.groupby([agrupar_por]).mean().reset_index()

    corr_matrix = df_agrupado[cols].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix,
                annot=True,            # Mostrar valores
                cmap='coolwarm',       # Colormap
                linewidths=0.5,        # Ancho de bordes
                fmt=".2f",             # Formato decimal
                annot_kws={"size": 10},
                vmin=-1, 
                vmax=1)       # Rango de colores = 1

    plt.title(titulo, pad = 20)
    plt.show()
    

# ==============================================================================
# Grafico interactivo de líneas
# ==============================================================================

def crear_graf_interactivo(dataframe):
    """
    Crea una interfaz interactiva para la función crear_graf_lineas
    
    Parámetros:
    -----------
    dataframe: pandas DataFrame
        El dataframe con los datos a visualizar
    
    Retorna:
    --------
    Un widget interactivo para visualizar los datos
    """
    # Función intermedia para usar con interact
    def actualizar_grafico(col_car1, col_car2, col_data, etiqueta_x, etiqueta_y, titulo):
        crear_graf_lineas(dataframe , col_car1, col_car2, col_data, etiqueta_x, etiqueta_y, titulo)
    
    # Crear los widgets
    columnas = list(dataframe.columns)
    
    col_car1_dropdown = widgets.Dropdown(
        options=columnas,
        description='Categoría:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    col_car2_dropdown = widgets.Dropdown(
        options=columnas,
        description='Tiempo:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    col_data_dropdown = widgets.Dropdown(
        options=columnas,
        description='Valor:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    etiqueta_x = widgets.Text(
        value='Año',
        description='Etiqueta X:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    etiqueta_y = widgets.Text(
        value='Valor',
        description='Etiqueta Y:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    titulo_widget = widgets.Text(
        value='Gráfico de líneas',
        description='Título:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='300px')
    )
    
    # Crear el widget interactivo
    interactive_plot = interactive(
        actualizar_grafico,
        col_car1=col_car1_dropdown,
        col_car2=col_car2_dropdown,
        col_data=col_data_dropdown,
        etiqueta_x=etiqueta_x,
        etiqueta_y=etiqueta_y,
        titulo=titulo_widget
    )
    
    # Organizar mejor la disposición
    inputs = VBox([
        HBox([col_car1_dropdown, col_car2_dropdown]),
        HBox([col_data_dropdown, etiqueta_x]),
        HBox([etiqueta_y, titulo_widget])
    ])
    
    # Retornar el widget completo
    return VBox([inputs, interactive_plot.children[-1]])