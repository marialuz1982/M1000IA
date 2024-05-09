import pandas as pd

# Cargar los archivos CSV
true_data = pd.read_csv(r'C:\Users\facus\OneDrive\Desktop\dataset fakeXpert\data\raw\True_converted.csv')
false_data = pd.read_csv(r'C:\Users\facus\OneDrive\Desktop\dataset fakeXpert\data\raw\Fake_converted.csv')

# Agregar una nueva columna indicando la fuente
true_data['label'] = 'True'
false_data['label'] = 'False'

# Concatenar los DataFrames
combined_data = pd.concat([true_data, false_data], ignore_index=True)

# Guardar el nuevo dataset unificado en un CSV
combined_data.to_csv(r'C:\Users\facus\OneDrive\Desktop\dataset fakeXpert\processed\combined_data.csv', index=False)
