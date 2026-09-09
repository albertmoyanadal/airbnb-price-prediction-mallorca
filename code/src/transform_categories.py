'''
Transformar les variables categòriques.
 - host_verifications → one-hot encoding
 - property_type → agrupar en 6 grups + one-hot encoding
 - room_type → one-hot encoding
 - amenities → 10 més freqüents + one-hot encoding
 - license → booleà (True si té llicència)
 - neighbourhood_cleansed → es manté com a descriptiva
'''


from ast import literal_eval

import pandas as pd

# Directoris
input_csv = "code/data/data_cleaning/listings_step2.csv"
output_csv = "code/data/data_cleaning/listings_step3.csv"
df = pd.read_csv(input_csv)


# Funcions
def parse_amenities(amenities_str):
    """Converteix string de amenities a llista."""
    if pd.isna(amenities_str):
        return []
    try:
        # Si és string, intentar convertir a llista
        if isinstance(amenities_str, str):
            # Netejar i convertir
            return literal_eval(amenities_str)
        return []
    except:  # noqa: E722
        return []

def get_property_group(property_type):
    """
    Agrupa property_type en 7 grups:
    - villa
    - house (cases, cottages, chalets, townhouses, etc.)
    - apartment (apartaments, condos, lofts, etc.)
    - private_room
    - shared_room
    - hotel (hotels, hostels, lodges)
    - other (camper, boat, castle, tiny home, etc.)
    """
    if pd.isna(property_type):
        return "other"
    
    p = str(property_type).lower()

    # 1. Habitacions (les més específiques primer)
    if "shared room" in p:
        return "shared_room"
    elif "private room" in p:
        return "private_room"
    
    # 2. Hotels i allotjaments similars
    elif "hotel" in p or "hostel" in p or "lodge" in p:
        return "hotel"
    
    # 3. Villas
    elif "villa" in p:
        return "villa"
    
    # 4. Cases (tots els tipus de cases)
    elif "entire home" in p or "entire house" in p or "entire cottage" in p or "entire chalet" in p or "cottage" in p or "chalet" in p or "townhouse" in p or "bungalow" in p or "cabin" in p or "vacation home" in p or "guesthouse" in p or "guest suite" in p or "casa particular" in p or "earthen home" in p or "entire place" in p:
        return "house"
    
    # 5. Apartaments
    elif "rental unit" in p or "apartment" in p or "condo" in p or "serviced apartment" in p or "aparthotel" in p or "flat" in p or "loft" in p:
        return "apartment"
    
    # 6. Altres (no classificats)
    elif "camper" in p or "rv" in p or "boat" in p or "farm stay" in p or "castle" in p or "island" in p or "tiny home" in p or "yurt" in p or "campsite" in p or "tower" in p:
        return "other"
    else:
        return "other"

# host_verifications → one-hot encoding

# Identificar tots els tipus de verificació possibles
verif_types = set()
for val in df['host_verifications'].dropna():
    try:
        if isinstance(val, str):
            lista = literal_eval(val)
            for item in lista:
                verif_types.add(item)
    except:  # noqa: E722, S110
        pass

# Crear una variable binària per a cada tipus de verificació
for vtype in verif_types:
    col_name = f"verif_{vtype}"
    df[col_name] = df['host_verifications'].apply(
        lambda x: bool(isinstance(x, str) and vtype in x)  # noqa: B023
    )
    count = df[col_name].sum()
    pct = (count / len(df)) * 100

# Eliminar la columna original
df.drop('host_verifications', axis=1, inplace=True)


# Transformar property_type

# Aplicar agrupació
df['property_group'] = df['property_type'].apply(get_property_group)

# Mostrar distribució
for group in sorted(df['property_group'].unique()):
    count = df[df['property_group'] == group].shape[0]
    pct = (count / len(df)) * 100

# One-hot encoding dels grups
dummies = pd.get_dummies(df['property_group'], prefix='prop')
df = pd.concat([df, dummies], axis=1)

# Eliminar columnes originals
df.drop(['property_type', 'property_group'], axis=1, inplace=True)


# room_type → one-hot encoding

dummies = pd.get_dummies(df['room_type'], prefix='room')
df = pd.concat([df, dummies], axis=1)

# Mostrar distribució
for col in dummies.columns:
    count = dummies[col].sum()
    pct = (count / len(df)) * 100
    print(f"      {col}: {count} ({pct:.1f}%)")

# Eliminar columna original
df.drop('room_type', axis=1, inplace=True)

# Transformar amenities → 10 més freqüents + one-hot encoding

# Convertir amenities a llista
df['amenities_list'] = df['amenities'].apply(parse_amenities)

# Comptar freqüència de cada amenity
amenity_counts = {}
for lista in df['amenities_list']:
    for item in lista:
        amenity_counts[item] = amenity_counts.get(item, 0) + 1

# Ordenar i seleccionar les 10 més freqüents
top_amenities = sorted(amenity_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("   Top 10 amenities més freqüents:")
for i, (amenity, count) in enumerate(top_amenities, 1):
    pct = (count / len(df)) * 100
    print(f"      {i}. {amenity}: {count} ({pct:.1f}%)")

# Crear variables binàries per a les top 10
for amenity, _ in top_amenities:
    col_name = f"amenity_{amenity.replace(' ', '_').replace('/', '_').lower()}"
    df[col_name] = df['amenities_list'].apply(lambda x: amenity in x if isinstance(x, list) else False)  # noqa: B023
    count = df[col_name].sum()
    pct = (count / len(df)) * 100
    print(f"      {col_name}: {count} ({pct:.1f}%)")

# Eliminar columnes originals
df.drop(['amenities', 'amenities_list'], axis=1, inplace=True)

# Transformar license → booleà (True si té llicència) 
has_license = df['license'].notna() & (df['license'] != '') & (df['license'] != 'NaN')
df['has_license'] = has_license

# Eliminar columna original
df.drop('license', axis=1, inplace=True)

# Guardar resultat
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
