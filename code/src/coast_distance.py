"""
Càlcul de la distància lineal a la costa utilitzant els límits municipals de l'IGN.
"""

import warnings

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import box

warnings.filterwarnings('ignore')

# Càrrega de dades

input_csv = "code/data/data_cleaning/listings_step5.csv"
output_csv = "code/data/data_cleaning/listings_step6.csv"
df = pd.read_csv(input_csv)



# CARREGAR I PROCESSAR LA COSTA DE MALLORCA


shapefile_path = (
    "code/data/recintos_municipales_inspire_peninbal_etrs89/"
    "recintos_municipales_inspire_peninbal_etrs89.shp"
)

municipis = gpd.read_file(shapefile_path)
print(f"   ✅ {len(municipis)} municipis carregats")
print(f"   📐 CRS original: {municipis.crs}")

# Filtrar només els municipis de Mallorca

# Utilitzem un bounding box aproximat de Mallorca
# (evita agafar Menorca, Eivissa, Formentera o la península)

mallorca_bbox = box(2.30, 39.20, 3.50, 39.95)
municipis_mallorca = municipis[municipis.intersects(mallorca_bbox)].copy()
print(f"   {len(municipis_mallorca)} municipis dins del bbox de Mallorca")


# Dissoldre tots els municipis en un sol polígon
# Com que Mallorca és una illa, el resultat serà el contorn de l'illa

illa_mallorca = municipis_mallorca.dissolve()
print(f"   Illa dissolta: {len(illa_mallorca)} polígon(s)")


# 2.3 Extreure la línia de costa (boundary exterior)

# Si la dissolució ha creat un MultiPolygon (per illots propers),
# agafem el polígon més gran (Mallorca)
geometria = illa_mallorca.geometry.iloc[0]
if geometria.geom_type == 'MultiPolygon':
    print("   ⚠️ MultiPolygon detectat, agafant el polígon més gran...")
    geometria = max(geometria.geoms, key=lambda p: p.area)

coastline = geometria.exterior
print(f"   Línia de costa obtinguda ({coastline.length:.2f} unitats)")


# Reprojectar a UTM 31N (EPSG:25831)

# Treballar en coordenades mètriques és MOLT més precís
# per calcular distàncies que en graus (EPSG:4326)

CRS_METRIC = "EPSG:25831"  # ETRS89 / UTM zone 31N (òptim per Mallorca)

# Crear GeoDataFrame de la costa i projectar
coastline_gdf = gpd.GeoDataFrame(
    geometry=[coastline],
    crs=municipis.crs
).to_crs(CRS_METRIC)

coastline_proj = coastline_gdf.geometry.iloc[0]
print(f"   Costa reprojectada a {CRS_METRIC}")


# CALCULAR DISTÀNCIA A LA COSTA (VECTORITZAT)


print("\nCalculant distància a la costa...")

# Convertir els listings en GeoDataFrame
gdf_listings = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['longitude'], df['latitude']),
    crs="EPSG:4326"
)

# Reprojectar a UTM 31N
gdf_listings = gdf_listings.to_crs(CRS_METRIC)

# Calcular distància (en metres) de cada punt a la línia de costa
# shapely ho fa element a element, però és ràpid (~segons)
gdf_listings['dist_sea_m'] = gdf_listings.geometry.distance(coastline_proj)

# Convertir a km
df['dist_sea_km'] = gdf_listings['dist_sea_m'].values / 1000

print(f"   dist_sea_km: min={df['dist_sea_km'].min():.3f}, "
      f"max={df['dist_sea_km'].max():.3f}, "
      f"mean={df['dist_sea_km'].mean():.3f}")

# Variable polinòmica (per capturar no-linealitats)
df['dist_sea_squared_km'] = df['dist_sea_km'] ** 2

# Variable logarítmica
df['dist_sea_log_km'] = np.log(df['dist_sea_km'] + 0.01)

print("   dist_sea_squared_km")
print("   dist_sea_log_km")

# Guardar el DataFrame amb la nova columna
df.to_csv(output_csv, index=False)



# Comprovar que els valors són raonables
print(df['dist_sea_km'].describe())

# Comprovar que cap valor és 0 o negatiu
print(f"Valors <= 0: {(df['dist_sea_km'] <= 0).sum()}")

# Comprovar el punt més proper a la costa
idx_min = df['dist_sea_km'].idxmin()
print(f"Punt més proper: {df.loc[idx_min, ['latitude', 'longitude', 'dist_sea_km']]}")

# Comprovar el punt més llunyà (hauria d'estar al centre de l'illa)
idx_max = df['dist_sea_km'].idxmax()
print(f"Punt més llunyà: {df.loc[idx_max, ['latitude', 'longitude', 'dist_sea_km']]}")










import matplotlib.pyplot as plt

# Crear figura
fig, ax = plt.subplots(figsize=(12, 10))

# Dibuixar la costa
coastline_gdf.plot(ax=ax, color='blue', linewidth=1, label='Costa')

# Dibuixar els listings (color segons distància)
gdf_listings.plot(
    ax=ax, 
    column='dist_sea_km', 
    cmap='viridis_r',  # Invertit: groc = a prop, blau = lluny
    markersize=3,
    legend=True,
    legend_kwds={'label': 'Distància a la costa (km)'}
)

ax.set_title('Distància a la costa dels Airbnb a Mallorca')
plt.tight_layout()
plt.savefig('code/outputs/map_dist_sea.png', dpi=500)
plt.show()