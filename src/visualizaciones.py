import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================================================================
# Funcióin para crear histogramas
# ==============================================================================

def crear_histograma(data, nombre_col, etiqueta_eje_x, etiqueta_eje_y):
    """
    Entradas:
        - data: Es la información que se va a graficar.
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

