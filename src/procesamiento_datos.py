import pandas as pd

categorias = [
    'Total Energy Consumption (TWh)',
    'Per Capita Energy Use (kWh)',
    'Renewable Energy Share (%)',
    'Fossil Fuel Dependency (%)',
    'Carbon Emissions (Million Tons)',
    'Energy Price Index (USD/kWh)'
]

# ==============================================================================
# Calculo de las medianas (máxima y minima) para cada categoría numerica
# ==============================================================================

def mediana_categoria(data, categorias):
    """
    Entradas:
        - data: Un dataframe de pandas.
        
    """
    # Calcular la mediana de cada categoría por país
    medianas_por_pais = data.groupby('Country')[categorias].median()

    resultados = {}

    for categoria in categorias:
        # Encontrar el país con la mediana más grande para la categoría actual
        pais_max_mediana = medianas_por_pais[categoria].idxmax()
        valor_max_mediana = medianas_por_pais[categoria].max()

        # Encontrar el país con la mediana más pequeña para la categoría actual
        pais_min_mediana = medianas_por_pais[categoria].idxmin()
        valor_min_mediana = medianas_por_pais[categoria].min()

        resultados[categoria] = {
            'Mediana más grande': (pais_max_mediana, valor_max_mediana),
            'Mediana más pequeña': (pais_min_mediana, valor_min_mediana)
        }

    # Imprimir los resultados
    for categoria, result in resultados.items():
        print(f"Categoría: {categoria}")
        print(f"  Mediana más grande: País = {result['Mediana más grande'][0]}, Valor = {result['Mediana más grande'][1]:.2f}")
        print(f"  Mediana más pequeña: País = {result['Mediana más pequeña'][0]}, Valor = {result['Mediana más pequeña'][1]:.2f}")
        print("-" * 55)


def top_mediana_categoria(data, categorias):
    """
    Entradas:
        - data: Un dataframe de pandas.
        
    """
    # Calcular la mediana de cada categoría por país
    medianas_por_pais = data.groupby('Country')[categorias].median()

    resultados = {}

    for categoria in categorias:
        # Encontrar el top 3 paises con la mediana más grande para la categoría actual
        top_3_max = medianas_por_pais[categoria].nlargest(3).index.tolist()
        top_3_max_valores = medianas_por_pais[categoria].nlargest(3).values.tolist()

        # Encontrar el top 3 paises con la mediana más pequeña para la categoría actual
        top_3_min = medianas_por_pais[categoria].nsmallest(3).index.tolist()
        top_3_min_valores = medianas_por_pais[categoria].nsmallest(3).values.tolist()

        resultados[categoria] = {
            'Top 3 Mediana más grande': list(zip(top_3_max, top_3_max_valores)),
            'Top 3 Mediana más pequeña': list(zip(top_3_min, top_3_min_valores))
        }

    # Imprimir los resultados
    for categoria, result in resultados.items():
        print(f"Categoría: {categoria}")
        print("  Top 3 Mediana más grande:")
        for pais, valor in result['Top 3 Mediana más grande']:
            print(f"    País = {pais}, Valor = {valor:.2f}")
        print("  Top 3 Mediana más pequeña:")
        for pais, valor in result['Top 3 Mediana más pequeña']:
            print(f"    País = {pais}, Valor = {valor:.2f}")
        print("-" * 55)   