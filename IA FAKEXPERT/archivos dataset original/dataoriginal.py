
import pandas as pd

# Cargar los archivos CSV
true_data = pd.read_csv(r'C:\Users\facus\OneDrive\Documents\M100O IA REPO\M1000IA\IA FAKEXPERT\archivos dataset original\True.csv')
false_data = pd.read_csv(r'C:\Users\facus\OneDrive\Documents\M100O IA REPO\M1000IA\IA FAKEXPERT\archivos dataset original\Fake.csv')

# Agregar una nueva columna indicando la fuente
true_data['label'] = 'True'
false_data['label'] = 'False'

# Concatenar los DataFrames
combined_data = pd.concat([true_data, false_data], ignore_index=True)

# Guardar el nuevo dataset unificado en un CSV
combined_data.to_csv(r'C:\Users\facus\OneDrive\Documents\M100O IA REPO\M1000IA\IA FAKEXPERT\archivos dataset original\unificado\unificado_data.csv', index=False)