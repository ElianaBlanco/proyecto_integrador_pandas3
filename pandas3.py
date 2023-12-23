import pandas as pd
from datasets import load_dataset

# Descarga y carga el dataset
dataset = load_dataset("mstz/heart_failure")

# Accede a la partición 'train' del dataset
data = dataset["train"]

# Convertir el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
cantidad_hombres_fumadores = df[(df['is_smoker'] == 1) & (df['is_male'] == 1)].shape[0]
cantidad_mujeres_fumadoras = df[(df['is_smoker'] == 1) & (df['is_male'] == 0)].shape[0]

print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
