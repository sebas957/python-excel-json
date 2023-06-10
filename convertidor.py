import pandas as pd
import json
from unidecode import unidecode

# Leer el archivo de Excel
df = pd.read_excel('/var/www/html/python-excel-json/ciudad.xlsx')

# Convertir los datos en una lista de diccionarios
data = []
for _, row in df.iterrows():
    item = {
        'model': row['model'],
        'pk': row['pk'],
        'fields': {
            'nombre': unidecode(row['nombre']),
            'codigo_postal': str(row['codigo_postal']).zfill(5),
            'latitud': row['latitud'],
            'longitud': row['longitud'],
            'estado': row['estado'],
        }
    }
    data.append(item)

# Convertir la lista de diccionarios en formato JSON
json_data = json.dumps(data, indent=4)

# Escribir el JSON en un archivo
with open('datos.json', 'w') as file:
    file.write(json_data)