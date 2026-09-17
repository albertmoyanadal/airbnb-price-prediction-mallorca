'''
Resum del fitxer listings.csv
 - Tipus de dada
 - Nombre total de files
 - Nombre de valors no nuls
 - Nombre de nuls
 - Percentatge de nuls
 El resultat es guarda en un fitxer CSV.
'''


# Llibreries
import pandas as pd

# Directori de les dades
input_csv = "code/data/data_raw/listings.csv"
#input_csv = "code/data/data_cleaning/listings_step5.csv"
df = pd.read_csv(input_csv)

# 3. MOSTRAR PER PANTALLA EL NOMBRE DE FILES I COLUMNES
print("Fitxer:")
print(f"Files:    {df.shape[0]}")
print(f"Columnes: {df.shape[1]}")
print()  # línia en blanc

# Resum
results = []

for columna in df.columns:
    # Tipus de dada
    types = str(df[columna].dtype)
    
    # Nombre de nuls (isnull().sum() compta els NaN)
    nuls = df[columna].isnull().sum()
    
    # Percentatge de nuls
    percent_nuls = (nuls / df.shape[0]) * 100
    
    # Diccionari amb les dades de la columna
    results.append({
        "Variable": columna,
        "Tipus": types,
        "Nuls": nuls,
        "Percentatge_nuls": round(percent_nuls, 2)  # arrodonit a 2 decimals
    })

df_result = pd.DataFrame(results)

output_excel = "code/data/data_raw/listings_resume.xlsx"
df_result.to_excel(output_excel, index=False, engine='openpyxl')

