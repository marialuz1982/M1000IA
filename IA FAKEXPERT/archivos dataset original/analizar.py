
import pandas as pd

# Rutas a los archivos CSV usando raw strings
path_original = r'IA FAKEXPERT\archivos dataset original\unificado\unificado_data.csv'
path_modified = r'IA FAKEXPERT\data\processed\combined_data.csv'

# Leer los datos y contar las filas
data_original = pd.read_csv(path_original)
data_modified = pd.read_csv(path_modified)

print("Entradas en el archivo original:", data_original.shape[0])
print("Entradas en el archivo modificado:", data_modified.shape[0])
