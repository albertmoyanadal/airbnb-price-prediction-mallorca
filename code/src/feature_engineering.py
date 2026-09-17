"""
Feature Engineering - Predicció de preus d'Airbnb a Mallorca.

Aquest script crea noves variables a partir de les dades netes:
    - Distància lineal a la costa (shapefile IGN)
    - Distàncies a punts d'interès (Palma, aeroport)
    - Índex de proximitat a platges populars
    - Índexs agregats (amenities, mida, accessibilitat)
    - Variables d'interacció
    - Característiques de barri
"""

import warnings

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from geopy.distance import geodesic
from shapely.geometry import box

warnings.filterwarnings('ignore')


# =============================================
# CONFIGURACIÓ
# =============================================

INPUT_CSV = "code/data/data_cleaning/listings_step4.csv"
OUTPUT_CSV = "code/data/data_cleaning/listings_step5.csv"
MAP_OUTPUT = "code/outputs/map_dist_sea.png"

SHAPEFILE_PATH = (
    "code/data/recintos_municipales_inspire_peninbal_etrs89/"
    "recintos_municipales_inspire_peninbal_etrs89.shp"
)

# ETRS89 / UTM zone 31N (òptim per Mallorca)
CRS_METRIC = "EPSG:25831"

# Punts clau a Mallorca (coordenades)
COORDINATES = {
    'palma_center': (39.5696, 2.6502),      # Plaça d'Espanya
    'airport': (39.5517, 2.7388),           # Aeroport Son Sant Joan
}




# =============================================
# FUNCIONS DE CÀLCUL
# =============================================

def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distància en km entre dos punts (fórmula de Haversine).
    """
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers


def load_mallorca_coastline(shapefile_path, crs_metric=CRS_METRIC):
    """
    Carrega els límits municipals de l'IGN i n'extreu la línia de costa
    de Mallorca, projectada a un CRS mètric.

    Returns:
        Tuple (coastline_gdf, coastline_proj)
            - coastline_gdf: GeoDataFrame amb la línia de costa en CRS original
            - coastline_proj: LineString projectada al CRS mètric
    """
    print("\nCarregant límits municipals de l'IGN...")
    municipis = gpd.read_file(shapefile_path)
    print(f"   {len(municipis)} municipis carregats")
    print(f"   CRS original: {municipis.crs}")

    # Filtrar només els municipis de Mallorca amb un bounding box aproximat
    # (evita agafar Menorca, Eivissa, Formentera o la península)
    mallorca_bbox = box(2.30, 39.20, 3.50, 39.95)
    municipis_mallorca = municipis[municipis.intersects(mallorca_bbox)].copy()
    print(f"   {len(municipis_mallorca)} municipis dins del bbox de Mallorca")

    # Dissoldre tots els municipis en un sol polígon.
    # Com que Mallorca és una illa, el resultat serà el contorn de l'illa.
    illa_mallorca = municipis_mallorca.dissolve()
    print(f"   Illa dissolta: {len(illa_mallorca)} polígon(s)")

    # Extreure la línia de costa (boundary exterior).
    # Si la dissolució ha creat un MultiPolygon (per illots propers),
    # agafem el polígon més gran (Mallorca).
    geometria = illa_mallorca.geometry.iloc[0]
    if geometria.geom_type == 'MultiPolygon':
        print("   MultiPolygon detectat, agafant el polígon més gran...")
        geometria = max(geometria.geoms, key=lambda p: p.area)

    coastline = geometria.exterior
    print(f"   Línia de costa obtinguda ({coastline.length:.2f} unitats)")

    # Reprojectar a UTM 31N (EPSG:25831)
    # Treballar en coordenades mètriques és MOLT més precís
    # per calcular distàncies que en graus (EPSG:4326)
    coastline_gdf = gpd.GeoDataFrame(
        geometry=[coastline],
        crs=municipis.crs
    ).to_crs(crs_metric)

    coastline_proj = coastline_gdf.geometry.iloc[0]
    print(f"   Costa reprojectada a {crs_metric}")

    return coastline_gdf, coastline_proj


def calculate_coast_distance(df, coastline_proj, coastline_gdf, crs_metric=CRS_METRIC):
    """
    Calcula la distància lineal (en km) de cada allotjament a la costa més propera.

    Retorna el DataFrame amb les noves variables i el GeoDataFrame dels
    listings projectat (per si es vol fer un mapa de validació).
    """
    print("\nCalculant distància a la costa...")

    # Convertir els listings en GeoDataFrame
    gdf_listings = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df['longitude'], df['latitude']),
        crs="EPSG:4326"
    )

    # Reprojectar a UTM 31N
    gdf_listings = gdf_listings.to_crs(crs_metric)

    # Calcular distància (en metres) de cada punt a la línia de costa.
    # shapely ho fa vectoritzat, és molt ràpid.
    gdf_listings['dist_sea_m'] = gdf_listings.geometry.distance(coastline_proj)

    # Convertir a km
    gdf_listings['dist_sea_km'] = gdf_listings['dist_sea_m'] / 1000   # ← NOVA
    df['dist_sea_km'] = gdf_listings['dist_sea_km'].values

    print(f"   dist_sea_km: min={df['dist_sea_km'].min():.3f}, "
          f"max={df['dist_sea_km'].max():.3f}, "
          f"mean={df['dist_sea_km'].mean():.3f}")

    # Variable polinòmica (per capturar no-linealitats)
    df['dist_sea_squared_km'] = df['dist_sea_km'] ** 2

    # Variable logarítmica
    df['dist_sea_log_km'] = np.log(df['dist_sea_km'] + 0.01)

    print("   dist_sea_squared_km")
    print("   dist_sea_log_km")

    return df, gdf_listings


def calculate_distances_to_points(df, lat_col='latitude', lon_col='longitude'):
    """
    Calcula distàncies a punts d'interès predefinits.
    """
    print("\nCalculant distàncies a punts d'interès...")

    # Distància a Palma centre
    df['dist_palma_center_km'] = df.apply(
        lambda row: haversine(
            row[lat_col], row[lon_col],
            COORDINATES['palma_center'][0], COORDINATES['palma_center'][1]
        ), axis=1
    )

    # Distància a l'aeroport
    df['dist_airport_km'] = df.apply(
        lambda row: haversine(
            row[lat_col], row[lon_col],
            COORDINATES['airport'][0], COORDINATES['airport'][1]
        ), axis=1
    )

    print("   dist_palma_center_km")
    print("   dist_airport_km")

    return df





def calculate_amenity_index(df):
    """
    Crea l'índex de serveis (AmenityIndex) a partir de les variables binàries
    d'amenities.
    """
    print("\nCreant índex de serveis...")

    # Índex de serveis (AmenityIndex)
    amenity_cols = [col for col in df.columns if col.startswith('amenity_')]
    if amenity_cols:
        df['amenity_index'] = df[amenity_cols].sum(axis=1)
        print(f"   amenity_index (suma de {len(amenity_cols)} amenities)")

    return df




def calculate_neighborhood_features(df):
    """
    Afegeix variables agregades per barri.
    """
    print("\nCalculant característiques de barri...")

    if 'neighbourhood_cleansed' not in df.columns:
        print("   No s'ha trobat neighbourhood_cleansed, saltant...")
        return df

    # Nombre d'anuncis per barri
    neighborhood_counts = (
        df.groupby('neighbourhood_cleansed')
        .size()
        .reset_index(name='num_listings_neighborhood')
    )
    df = df.merge(neighborhood_counts, on='neighbourhood_cleansed', how='left')
    print("   num_listings_neighborhood")

    # Preu mitjà per barri (si tenim price)
    if 'price' in df.columns:
        neighborhood_prices = (
            df.groupby('neighbourhood_cleansed')['price']
            .mean()
            .reset_index(name='avg_price_neighborhood')
        )
        df = df.merge(neighborhood_prices, on='neighbourhood_cleansed', how='left')
        print("   avg_price_neighborhood")

    # Preu mitjà del barri com a ràtio sobre el preu de l'apartament
    if 'price' in df.columns and 'avg_price_neighborhood' in df.columns:
        df['price_ratio_vs_neighborhood'] = df['price'] / df['avg_price_neighborhood']
        print("   price_ratio_vs_neighborhood")

    return df


def plot_coast_distance_map(gdf_listings, coastline_gdf, output_path=MAP_OUTPUT):
    """
    Genera un mapa de validació amb la costa i els listings acolorits
    segons la seva distància al mar.
    """
    print("\nGenerant mapa de validació...")

    _fig, ax = plt.subplots(figsize=(12, 10))

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
    plt.savefig(output_path, dpi=500)
    plt.close()

    print(f"   Mapa guardat a: {output_path}")


# =============================================
# EXECUCIÓ PRINCIPAL
# =============================================

def main():
    print("=" * 60)
    print(" FEATURE ENGINEERING - PREDICCIÓ PREUS AIRBNB MALLORCA")
    print("=" * 60)

    # Carregar dades
    print("\nCarregant dades...")
    df = pd.read_csv(INPUT_CSV)
    print(f"Files: {len(df)} | Columnes: {len(df.columns)}")

    # 1. Carregar la costa de Mallorca (shapefile IGN)
    coastline_gdf, coastline_proj = load_mallorca_coastline(SHAPEFILE_PATH)

    # 2. Distància lineal a la costa
    df, gdf_listings = calculate_coast_distance(df, coastline_proj, coastline_gdf)

    # 3. Distàncies a punts d'interès
    df = calculate_distances_to_points(df)

    # 4. Índexs agregats
    df = calculate_amenity_index(df)

    # 5. Característiques de barri
    df = calculate_neighborhood_features(df)

    # Guardar resultats
    print("\nGuardant resultats...")
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"\nFitxer guardat: {OUTPUT_CSV}")
    print(f"Files: {len(df)} | Columnes: {len(df.columns)}")

    # Resum de les noves variables creades
    print("\n" + "=" * 60)
    print(" NOVES VARIABLES CREADES")
    print("=" * 60)
    new_cols = [
        'dist_sea_km', 'dist_sea_squared_km', 'dist_sea_log_km',
        'dist_palma_center_km', 'dist_airport_km',
        'amenity_index', 
        'num_listings_neighborhood', 'avg_price_neighborhood',
        'price_ratio_vs_neighborhood',
    ]

    existing_new = [col for col in new_cols if col in df.columns]
    print(f"{len(existing_new)} variables afegides:")
    for col in existing_new:
        print(f"   - {col}: min={df[col].min():.2f}, "
              f"max={df[col].max():.2f}, mean={df[col].mean():.2f}")

    # Mapa de validació
    plot_coast_distance_map(gdf_listings, coastline_gdf)

    print("\nFeature Engineering completat!")


if __name__ == "__main__":
    main()