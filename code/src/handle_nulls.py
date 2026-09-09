'''
Tractar els valors nuls.
- Eliminar files amb nuls en variables crítiques (poques observacions)
- Omplir amb mediana les variables de review scores (molts nuls)
'''

import pandas as pd

# Directoris
input_csv = "code/data/data_cleaning/listings_step3.csv"
output_csv = "code/data/data_cleaning/listings_step4.csv"

# Llegir fitxer
df = pd.read_csv(input_csv)

# Mostrar nuls per variable
print("\nValors nuls per variable:")
nuls = df.isnull().sum()
nuls_pct = (nuls / len(df)) * 100
nuls_df = pd.DataFrame({
    'Variable': nuls.index,
    'Nuls': nuls.values,
    'Percentatge': nuls_pct.values
})
nuls_df = nuls_df[nuls_df['Nuls'] > 0].sort_values('Nuls', ascending=False)
print(nuls_df.to_string(index=False))

# Eliminar files amb pocs nuls

# Variables on volem eliminar files amb nuls (poques observacions)
critical_vars = [
    'host_response_rate',
    'host_acceptance_rate',
    'beds',
    'estimated_revenue_l365d',
    'price',
    'host_since',
    'host_listings_count',
    'bathrooms',
    'bedrooms'
]

# Comptar quantes files teníem abans
rows_before = df.shape[0]

# Eliminar files amb nuls en aquestes variables
df = df.dropna(subset=critical_vars)


# Omplim nuls de review scores amb mediana (molts nuls)
print("\n Omplint nuls de review scores amb mediana...")

# Variables de review scores
review_vars = [
    'review_scores_rating',
    'review_scores_accuracy',
    'review_scores_cleanliness',
    'review_scores_checkin',
    'review_scores_communication',
    'review_scores_location',
    'review_scores_value'
]

# Crear variable booleana: True si té ressenyes (cap nul), False si no en té
df['has_reviews'] = df[review_vars].notna().all(axis=1)

# Comptar quants en tenen i quants no
has_reviews_count = df['has_reviews'].sum()
no_reviews_count = len(df) - has_reviews_count
print(f"   Té ressenyes: {has_reviews_count} ({has_reviews_count/len(df)*100:.1f}%)")
print(f"   No té ressenyes: {no_reviews_count} ({no_reviews_count/len(df)*100:.1f}%)")

for col in review_vars:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        print(f"   {col}: omplert amb mediana ({median_val:.2f})")

# Comprovar nuls restants
print("\nNuls restants per variable:")
nuls_restants = df.isnull().sum()
nuls_restants = nuls_restants[nuls_restants > 0]
if len(nuls_restants) == 0:
    print("   No queden nuls!")
else:
    print(nuls_restants)

# Guardar
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"\nFitxer guardat a: {output_csv}")
print(f"   → {df.shape[0]} files i {df.shape[1]} columnes.")