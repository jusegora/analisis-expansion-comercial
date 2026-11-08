import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import folium
import os

def run_geo():
    np.random.seed(42)
    n = 50
    
    # Datos simulados
    flujo = np.random.randint(1000, 15000, n)
    estrato = np.random.choice([1, 2, 3, 4], n, p=[0.3, 0.4, 0.2, 0.1])
    arriendo = (flujo * 0.05) + (estrato * 2) + np.random.normal(0, 5, n)
    
    lat_c, lon_c = 4.59, -74.14
    lat = np.random.normal(lat_c, 0.05, n)
    lon = np.random.normal(lon_c, 0.05, n)

    df = pd.DataFrame({
        'Barrio': [f"Barrio Sur {i}" for i in range(1, n + 1)],
        'Flujo': flujo,
        'Estrato': estrato,
        'Arriendo': arriendo,
        'Lat': lat,
        'Lon': lon
    })

    # KMeans
    X = df[['Flujo', 'Estrato', 'Arriendo']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Identificar mejor cluster
    resumen = df.groupby('Cluster').mean(numeric_only=True)
    best_cluster = resumen['Flujo'].idxmax()
    
    df['Potencial'] = df['Cluster'].apply(lambda x: 'ALTO' if x == best_cluster else 'BAJO')

    print(df['Potencial'].value_counts())
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/barrios.csv', index=False)

    # Mapa
    mapa = folium.Map(location=[lat_c, lon_c], zoom_start=12)
    for idx, row in df.iterrows():
        color = 'green' if row['Potencial'] == 'ALTO' else 'red'
        folium.Marker(
            [row['Lat'], row['Lon']],
            popup=f"{row['Barrio']} - Flujo: {row['Flujo']}",
            icon=folium.Icon(color=color, icon='store', prefix='fa')
        ).add_to(mapa)
        
    mapa.save('mapa_geo.html')
    print("Mapa guardado.")

if __name__ == "__main__":
    run_geo()
