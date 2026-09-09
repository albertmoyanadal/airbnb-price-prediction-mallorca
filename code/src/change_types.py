'''
Segona etapa de neteja: canviar els tipus de les variables segons el fitxer de resum.
Llegeix el CSV de l'etapa 1, aplica les conversions (int, float, datetime, bool), i guarda el resultat a la carpeta data_cleaning. 
'''


import numpy as np
import pandas as pd

# Directoris
input_csv = "code/data/data_cleaning/listings_step1.csv"
input_excel = "code/data/data_summary.xlsx"
output_csv = "code/data/data_cleaning/listings_step2.csv"

# Llegir fitxers
df = pd.read_csv(input_csv)
df_summary = pd.read_excel(input_excel, sheet_name="listings")
df_summary.columns = df_summary.columns.str.strip()

# Diccionari de conversions: {variable: tipus}
conv_dict = {}
for _, row in df_summary.iterrows():
    var = row["Variable"]
    target = row["Canviar tipus"]
    if var in df.columns and pd.notna(target) and target != "No" and target != "Mirar categories":
        conv_dict[var] = target

print(f"\n Variables a convertir: {len(conv_dict)}")
for v, t in conv_dict.items():
    print(f"   {v} → {t}")




# ==========================================
# FUNCIONS DE CONVERSIÓ
# ==========================================


def to_bool(value):
    """Converteix 't'/'f' a booleà (True/False)."""
    if pd.isna(value):
        return np.nan
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        v = value.strip().lower()
        if v in ['t', 'true', '1', 'yes', 'y']:
            return True
        if v in ['f', 'false', '0', 'no', 'n']:
            return False
        return np.nan
    return np.nan


def to_float_percent(value):
    """Converteix '100%' a 1.0, '50%' a 0.5, etc."""
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value) / 100  # Si ja és número, el dividim per 100
    if isinstance(value, str):
        clean = value.replace('%', '').strip()
        try:
            return float(clean) / 100  # Dividim per 100 per obtenir proporció
        except:  # noqa: E722
            return np.nan
    return np.nan



def to_price(value):
    """Converteix '$164.00' a float (164.0)."""
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        clean = value.replace('$', '').replace(',', '').strip()
        try:
            return float(clean)
        except:  # noqa: E722
            return np.nan
    return np.nan

# Aplicam les conversions segons el diccionari

for var, target in conv_dict.items():
    print(f"   Convertint {var} → {target}...")
    
    if target == "datetime":
        df[var] = pd.to_datetime(df[var], errors='coerce')
    
    elif target == "float":
        if var == "price":
            df[var] = df[var].apply(to_price)
        elif var in ["host_response_rate", "host_acceptance_rate"]:
            df[var] = df[var].apply(to_float_percent)
        else:
            df[var] = pd.to_numeric(df[var], errors='coerce')
    
    elif target == "int":
        # Convertim a numèric i després a Int64 (accepta NaN)
        df[var] = pd.to_numeric(df[var], errors='coerce')
        # Si tots els decimals són .0, convertim a int
        non_null = df[var].dropna()
        if len(non_null) == 0 or (non_null % 1 == 0).all():
            df[var] = df[var].astype('Int64')
        # Si no, deixem com a float
    
    elif target == "bool":
        df[var] = df[var].apply(to_bool)
        df[var] = df[var].astype('bool')
    
    else:
        print(f"Tipus '{target}' no reconegut. No es modifica.")

# Guardam el resultat
print(f"\nGuardant el fitxer a: {output_csv}")
df.to_csv(output_csv, index=False, encoding='utf-8-sig')

# Mostrar un resum dels tipus nous
print("\nTipus de variables després de la conversió:")
for col in df.columns:
    print(f"   {col}: {df[col].dtype}")


    
