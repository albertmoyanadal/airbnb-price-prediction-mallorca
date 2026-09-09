'''
Primera etapa de neteja: eliminar variables que no es mantenen segons el fitxer de resum.

legeix el CSV raw i el fitxer Excel, filtra les columnes amb "Mantenir = Sí", i guarda el resultat a la carpeta data_cleaning
'''


import pandas as pd

# Directoris

input_csv = "code/data/data_raw/listings.csv"
input_excel = "code/data/data_summary.xlsx"
output_csv = "code/data/data_cleaning/listings_step1.csv"

# Llegir fitxers
df_raw = pd.read_csv(input_csv)
df_summary = pd.read_excel(input_excel, sheet_name="listings")

# Netejar noms de columnes de l'Excel per evitar espais
df_summary.columns = df_summary.columns.str.strip()

# Seleccionar variables a mantenir
keep_vars = df_summary[df_summary["Mantenir"] == "Sí"]["Variable"].tolist()

print(f"\n Variables a mantenir: {len(keep_vars)}")
print("   " + ", ".join(keep_vars))

# Filtrem el DataFrame per les columnes seleccionades
df_filtered = df_raw[keep_vars].copy()

print(f"\n DataFrame filtrat: {df_filtered.shape[0]} files i {df_filtered.shape[1]} columnes.")

# Guardar el .csv filtrat
df_filtered.to_csv(output_csv, index=False, encoding='utf-8-sig')
