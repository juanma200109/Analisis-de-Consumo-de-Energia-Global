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
    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_correlación_" + titulo.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
    # Mostrar el gráfico
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

# ==============================================================================
# Grafico de barras agrupadas
# ==============================================================================
def crear_grafico_barras_agrupadas(data, col_grup,col_categoria, col_subcategoria, nombre_variable, col_valor, etiqueta_x, etiqueta_y, titulo):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - col_grup: Nombre de la columna que se va a graficar (grupo, ej: 'Country').
        - col_categoria: Nombre de la columna que se va a graficar (categoría principal, 'Renewable Energy Share (%)').
        - col_subcategoria: Nombre de la columna que se va a graficar (subcategoría, ej: Fossil Fuel Dependency (%)).
        - nombre_variable: Nombre de la variable que se va a graficar (categoría, ej: Tipo de Energía).
        - col_valor: Nombre de la columna que se va a graficar (valores, ej: 'Porcentaje').
        - etiqueta_x: Etiqueta del eje x (ej: 'País').
        - etiqueta_y: Etiqueta del eje y (ej: 'Porcentaje (%)').
        - titulo: Título del gráfico 'Distribución de Tipos de Energía por País'.

    Salida:
        - Un gráfico de barras agrupadas que muestra la relación entre las dos variables.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """
    df_tipo_energia = data.groupby(col_grup)[[col_categoria, col_subcategoria]].mean().reset_index()

    # Apilando el dataframe para crear un gráfico de barras
    tabla_apilada = df_tipo_energia.melt(id_vars=[col_grup], var_name=nombre_variable, value_name=col_valor)

    plt.figure()
    sns.barplot(data=tabla_apilada, x=col_grup, y=col_valor, hue=nombre_variable, palette="Set2")
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.xticks(rotation=90)
    plt.legend(title=nombre_variable)
    plt.tight_layout()

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_barras_agrupadas_" + col_valor.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)

    plt.show()

# ==============================================================================
# Grafico de dispersión
# ==============================================================================
def crear_grafico_dispersion_por_año(data, col_categoria, col_subcategoria, año, col_x, col_y, etiqueta_x, etiqueta_y, titulo):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - col_categoria: Nombre de la columna que se va a graficar (grupo, ej: 'Country').
        - col_subcategoria: Nombre de la columna que se va a graficar (grupo, ej: 'Year').
        - año: Año que se va a graficar (ej: '2020').
        - col_x: Nombre de la columna que se va a graficar en el eje x (ej: 'Total Energy Consumption (TWh)').
        - col_y: Nombre de la columna que se va a graficar en el eje y (ej: 'Carbon Emissions (Million Tons)').
        - etiqueta_x: Etiqueta del eje x.
        - etiqueta_y: Etiqueta del eje y.
        - titulo: Título del gráfico (ej: 'Relación entre el Consumo Total de Energía y las Emisiones de Carbono por País').

    Salida:
        - Un gráfico de dispersión que muestra la relación entre las dos variables.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """
    # Agrupando los datos segun las columnas de categoria y subcategoria
    data_agrupada = data.groupby([col_categoria, col_subcategoria])[[col_x, col_y]].sum().reset_index()

    # Filtrando los datos para el año seleccionado
    data_filtrada = data_agrupada[data_agrupada[col_subcategoria] == int(año)]

    # Ordenando los datos por el eje x
    data_filtrada = data_filtrada.sort_values(by=col_x)

    x = data_filtrada[col_x]
    y = data_filtrada[col_y]
    etiquetas = data_filtrada[col_categoria]

    colors = plt.cm.tab10(np.linspace(0, 1, len(etiquetas)))

    plt.figure()

    for i, etiqueta in enumerate(etiquetas):
        plt.scatter(x.iloc[i], y.iloc[i], color=colors[i], label=etiqueta, alpha=0.8, edgecolors='black')
        plt.text(x.iloc[i], y.iloc[i], etiqueta, fontsize=8, ha='right', va='bottom') # Añadir etiquetas a los puntos

    plt.title(titulo+" - "+año, fontsize=16)
    plt.xlabel(etiqueta_x+" - "+año, fontsize=12)
    plt.ylabel(etiqueta_y+" - "+año, fontsize=12)
    plt.xticks(rotation=90)
    plt.grid(True, alpha=0.7, color='gray', linestyle='-', linewidth=0.5)
    plt.tight_layout()

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_dispersion_" + col_y.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_") + "_" + año
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)

    plt.show()


def crear_grafico_dispersion(data, col_grup, col_x, col_y, etiqueta_x, etiqueta_y, titulo):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - col_grup: Nombre de la columna que se va a graficar (grupo, ej: 'Country').
        - col_x: Nombre de la columna que se va a graficar en el eje x (ej: 'Total Energy Consumption (TWh)').
        - col_y: Nombre de la columna que se va a graficar en el eje y (ej: 'Carbon Emissions (Million Tons)').
        - etiqueta_x: Etiqueta del eje x.
        - etiqueta_y: Etiqueta del eje y.
        - titulo: Título del gráfico (ej: 'Relación entre el Consumo Total de Energía y las Emisiones de Carbono por País').

    Salida:
        - Un gráfico de dispersión que muestra la relación entre las dos variables.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """

    x = data.groupby(col_grup)[col_x].sum().sort_values() # Sumar el consumo total de energía por país y ordenar

    y = data.groupby(col_grup)[col_y].sum().loc[x.index] # Sumar las emisiones de carbono por país y ordenar según el índice de x

    paises = x.index # Obtener los nombres de los países ordenados

    # Generar una lista de 10 colores únicos
    num_paises = len(paises)
    colores = plt.cm.tab10(np.linspace(0, 1, num_paises)) # Usamos un mapa de colores para obtener colores distintos

    plt.figure()

    for i, pais in enumerate(paises):
        plt.scatter(x[pais], y[pais], color=colores[i], label=pais, alpha=0.7, edgecolors = 'black') # Graficar cada país con su respectivo color
        plt.text(x[pais], y[pais], pais, fontsize=8, ha='right', va='bottom') # Añadir etiquetas a los puntos

    plt.title(titulo, fontsize=16)
    plt.xlabel(etiqueta_x, fontsize=12)
    plt.ylabel(etiqueta_y, fontsize=12)
    plt.xticks(rotation=90)
    plt.grid(True, alpha=0.7, color='gray', linestyle='-', linewidth=0.5)
    plt.tight_layout()

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)
    
    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_dispersion_" + col_y.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")
    
    plt.savefig(ruta_completa)

    plt.show()

# ==============================================================================
# Gráfico de pastel
# ==============================================================================
def crear_grafico_pastel(data, filtro, col_categoria, col_subcategoria, titulo, filas, columnas):
    """
    Entradas:
        - data: Es la información que se va a graficar (dataframe).
        - filtro: Filtro para la categoría (ej: 'Country').
        - col_categoria: Nombre de la columna que se va a graficar (grupo, ej: 'Industrial Energy Use (%)').
        - col_subcategoria: Nombre de la columna que se va a graficar (grupo, ej: 'Household Energy Use (%)').
        - titulo: Título del gráfico (ej: 'Distribución de Tipos de Energía por País').

    Salida:
        - Un gráfico de pastel que muestra la relación entre las dos variables.
        - El gráfico se guarda como un archivo PNG en la ruta '../reporte/figuras/'
          con un nombre de archivo generado a partir del nombre de la columna del eje y.
        - El gráfico también se muestra en pantalla.
    """
    list_data = data[filtro].unique()
    num = len(list_data)

    # Número de filas y columnas para la cuadrícula
    fil = filas
    col = columnas

    # Crear una figura y los subgráficos
    fig, axs = plt.subplots(nrows = fil, ncols = col, figsize=(12, 15))
    axs = axs.flatten() # Aplanar la matriz de ejes para facilitar el acceso a cada subgráfico

    for i, caracteristica in enumerate(list_data):
        if i < fil * col:
            # Filtrar los datos para la característica actual
            data_filtrada = data[data[filtro] == caracteristica]

            # Promedio de la categoria y subcategoría
            data_category = data_filtrada[col_categoria].mean()
            data_subcategory = data_filtrada[col_subcategoria].mean()

            valores = [data_category, data_subcategory]

            # Crear el gráfico de pastel
            axs[i].pie(valores, autopct='%1.1f%%', startangle=90, colors=['#009688','#23bac4'])
            axs[i].set_title(f"{titulo} {caracteristica}")
            axs[i].axis('equal')
    etiquetas = [col_categoria, col_subcategoria]
    if num < fil * col:
        for j in range(num, filas * columnas):
            fig.delaxes(axs[j])

    # Crear directorio si no existe
    ruta_figura = os.path.join('..', 'reporte', 'figuras')
    os.makedirs(ruta_figura, exist_ok=True)

    # Nombre del archivo limpio (sin caracteres especiales)
    nombre_archivo = "Grafico_de_pastel_" + col_categoria.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    ruta_completa = os.path.join(ruta_figura, nombre_archivo + ".png")


    fig.legend(labels=etiquetas, loc='center right', bbox_to_anchor=(1.1, 1.0))
    plt.tight_layout()
    plt.savefig(ruta_completa)

    plt.show()