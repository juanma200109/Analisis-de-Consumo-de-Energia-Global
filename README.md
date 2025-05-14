# Consumo de Energía Global (2000-2024)

## 1. Descripción del Proyecto

Este proyecto profundiza en veinte años de datos de consumo energético a nivel global, desglosado por país y sector (industrial y doméstico). Su objetivo principal es evaluar las tendencias históricas del consumo, analizar la velocidad y el grado de adopción de energías renovables en contraposición a la dependencia de combustibles fósiles, y cuantificar la relación entre estos patrones de consumo y las emisiones de $\text{CO}_2$ generadas. Además, se explorarán las disparidades regionales en la transición energética y se buscarán posibles correlaciones con factores económicos, geográficos y de políticas energéticas implementadas en cada nación.

## 2. Motivación y Objetivos

Las motivaciones para este proyecto son:

- **Importancia de la Energía:** El suministro de energía a los hogares, comercios e industrias a impulsado el desarrollo en diferentes aspecto tanto socioeconómicos, industrial y la calidad de vida. Mejorando las condiciones para los trabajadores, personas del comun y en general a todos ya que gracias a la energía se han desarrollado maquinas capaces de mejorar las condiciones de vida como por ejemplo los electrodomesticos, computadoras, etc.
<br>
- **Transición Energética:** Desde hace decadas se viene mencionando la necesidad de mejorar las practicas de producción de energía, dado que las tradicionales dependientes de combustibles fósiles han perjudicado el medio ambiente, empeorando la calidad del aire, destruyendo la capa de ozono y provocando el conocido **Calentamiento Global**. Dado lo anterior se demuestra la importancia de diversificar la matriz energética introduciendo fuentes de energía sostenible (solar, eolica, etc.), velando por la seguridad energética y comprendiendo que los recursos fósiles son agotables.

Los objetivos principales de este proyecto son:

- **Analizar** la evolución del consumo energético global y por sector (industrial y doméstico) durante el periodo 2000-2024, identificando tasas de crecimiento y cambios estructurales.

- **Evaluar** la penetración de las energías renovables en el mix energético de los principales países consumidores y determinar la velocidad de esta transición.

- **Explorar** la posible influencia de variables económicas, geográficas y de políticas energéticas en la adopción de fuentes de energía renovable.

- **Cuantificar** la dependencia de los combustibles fósiles en el contexto del aumento de las energías renovables, identificando países con una mayor y menor inercia en su matriz energética.

- **Determinar** la correlación entre el consumo energético (por fuente y sector) y las emisiones de dióxido de carbono a nivel nacional.

## 3. Estructura del Repositorio
```text
├── data/
│   ├── dataset_limpio/
│   ├── dataset_original/
│   │   └── global_energy_consumption.csv
├── notebooks/
│   └── Consumo_de_Energia_Global_2000-2024.ipynb
├── reporte/
│   └── figuras/
├── src/
│   ├── __init__.py
│   ├── procesamiento_datos.py
│   └── visualizaciones.py
├── .gitignore
├── LICENCE
├── README.md
├── requirements.txt
```
## 4. Fuentes de Datos

- [Global Energy Consumption (2000-2024)](https://www.kaggle.com/datasets/atharvasoundankar/global-energy-consumption-2000-2024)

## 5. Visualización y Reportes

Carpeta `reports/` con gráficos de series temporales, mapas de calor y dashboards.

## 6. Licencia

Este proyecto está bajo la licencia **Apache-2.0 license**

## 7. Autor

- Juan Manuel Martínez Estrada
- manuel.martinez1@utp.edu.co
- [LinkedIn](https://www.linkedin.com/in/juan-manuel-martinez-estrada-8b17b2292/)