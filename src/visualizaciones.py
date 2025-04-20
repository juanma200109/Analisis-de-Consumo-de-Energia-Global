import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    salida: Un gráfico con un histograma.
    """
    plt.hist(data[nombre_col], bins=24, alpha=0.5, color='blue',  edgecolor='black')
    plt.xlabel(etiqueta_eje_x)
    plt.ylabel(etiqueta_eje_y)
    plt.title('Histograma de ' + nombre_col)
    plt.show()

# ==============================================================================
# Función para crear un grafico KDE (similar a la función de densidad de probabilidad)
# ==============================================================================

def crear_grafico_kde(data, nombre_col, etiqueta_eje_x, etiqueta_eje_y):
    """
    Entradas: 
        - data: Es la información que se va a graficar.
        - nombre_col: Nombre de la columna que se va a graficar.
        - etiqueta_eje_x: Es la etiqueta del eje x.
        - etiqueta_eje_y: Es la etiqueta del eje y.
    Salida: Un gráfico con un grafico KDE.
    """
    sns.kdeplot(data[nombre_col], fill=True, color='skyblue')
    plt.title('Grafico KDE de ' + nombre_col)
    plt.xlabel(etiqueta_eje_x)
    plt.ylabel(etiqueta_eje_y)
    plt.show()

# ==============================================================================
# Bloxplot
# ==============================================================================
