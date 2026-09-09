'''
Tercera etapa de neteja: explorar les categories de les variables amb "Mirar categories".

Llegeix el CSV de l'etapa 2 i el fitxer de resum, identifica les variables amb "Mirar categories", i permet seleccionar-ne una per veure totes les seves categories amb recompte i percentatge.
'''


import pandas as pd

# Directoris
input_csv = "code/data/data_cleaning/listings_step2.csv"
input_excel = "code/data/data_summary.xlsx"

df = pd.read_csv(input_csv)
df_summary = pd.read_excel(input_excel, sheet_name="listings")
df_summary.columns = df_summary.columns.str.strip()

# Variables amb categories
category_vars = []
for _, row in df_summary.iterrows():
    var = row["Variable"]
    target = row["Canviar tipus"]
    if var in df.columns and pd.notna(target) and target == "Mirar categories":
        category_vars.append(var)

print(f"\nVariables amb 'Mirar categories': {len(category_vars)}")
for i, var in enumerate(category_vars, 1):
    # Comptem quantes categories té (valors únics)
    n_categories = df[var].nunique()
    print(f"   {i}. {var} ({n_categories} categories)")

# Selecció de variable per explorar
print("\n" + "="*50)
print("Selecciona una variable per veure les seves categories:")
print("   (escriu el número o 'q' per sortir)")

while True:
    try:
        seleccio = input("\nNúmero de variable: ").strip()
        
        if seleccio.lower() == 'q':
            print("Sortint...")
            break
        
        # Convertir a enter i comprovar que és vàlid
        idx = int(seleccio) - 1
        if idx < 0 or idx >= len(category_vars):
            print(f"   Número no vàlid. Tria entre 1 i {len(category_vars)}")
            continue
        
        var = category_vars[idx]
        
        # Categories de la variable seleccionada
        print("\n" + "="*50)
        print(f"Categories de la variable: {var}")
        print("="*50)
        
        # Calcular recompte i percentatge de cada categoria
        counts = df[var].value_counts(dropna=False)
        total = len(df[var])
        
        # Crear una taula per mostrar
        print(f"\n{'Categoria':<40} {'Recompte':>10} {'Percentatge':>12}")
        print("-"*62)
        
        for categoria, recompte in counts.items():
            # Gestionar el cas de NaN
            if pd.isna(categoria):
                categoria_str = "NaN"
            else:
                categoria_str = str(categoria)[:38]  # Limitar longitud per a la taula
            
            percentatge = (recompte / total) * 100
            print(f"{categoria_str:<40} {recompte:>10} {percentatge:>11.2f}%")
        
        print("-"*62)
        print(f"{'TOTAL':<40} {total:>10} {100.00:>11.2f}%")
        
        # Estadístiques addicionals
        print("\nEstadístiques:")
        print(f"   • Categories úniques: {len(counts)}")
        print(f"   • Valors no nuls: {df[var].count()}")
        print(f"   • Valors nuls (NaN): {df[var].isna().sum()}")
        
        # Mostrar les 5 categories més freqüents
        print("\nTop 5 categories més freqüents:")
        for i, (cat, count) in enumerate(counts.head(5).items(), 1):
            pct = (count / total) * 100
            cat_str = "NaN" if pd.isna(cat) else str(cat)[:30]
            print(f"      {i}. {cat_str}: {count} ({pct:.1f}%)")
        
        print("\n" + "="*50)
        print("Prem Enter per continuar o escriu 'q' per sortir.")
        
    except ValueError:
        print("   Si us plau, introdueix un número vàlid.")
    except KeyboardInterrupt:
        print("\n\nSortint...")
        break

