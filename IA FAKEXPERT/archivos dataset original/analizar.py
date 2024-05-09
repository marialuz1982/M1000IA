
import pandas as pd

# Rutas a los archivos CSV usando raw strings
path_original = r'C:\Users\facus\OneDrive\Desktop\dataset fakeXpert\original\combined_data_original.csv'
path_modified = r'C:\Users\facus\OneDrive\Desktop\dataset fakeXpert\processed\combined_data.csv'

# Leer los datos y contar las filas
data_original = pd.read_csv(path_original)
data_modified = pd.read_csv(path_modified)

print("Entradas en el archivo original:", data_original.shape[0])
print("Entradas en el archivo modificado:", data_modified.shape[0])
