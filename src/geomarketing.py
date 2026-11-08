import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import folium
import os

def analizar_geografia():
    print("Iniciando Analisis de Geomarketing para el Sur de Bogota...")
    
    np.random.seed(42)
    n_barrios = 50
    barrios = [f"Barrio Sur {i}" for i in range(1, n_barrios + 1)]
    
    flujo = np.random.randint(1000, 15000, n_barrios)
    estrato = np.random.choice([1, 2, 3, 4], n_barrios, p=[0.3, 0.4, 0.2, 0.1])
    costo_arriendo = (flujo * 0.05) + (estrato * 2) + np.random.normal(0, 5, n_barrios)
    
    lat_center, lon_center = 4.59, -74.14
    lat = np.random.normal(lat_center, 0.05, n_barrios)
    lon = np.random.normal(lon_center, 0.05, n_barrios)

    df = pd.DataFrame({
        'Barrio': barrios,
        'Flujo_Peatonal': flujo,
        'Estrato': estrato,
        'Costo_Arriendo_Millones': costo_arriendo,
        'Latitud': lat,
        'Longitud': lon
    })

    X = df[['Flujo_Peatonal', 'Estrato', 'Costo_Arriendo_Millones']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    resumen = df.groupby('Cluster').mean(numeric_only=True)
    cluster_oro = resumen['Flujo_Peatonal'].idxmax()
    
    df['Potencial'] = df['Cluster'].apply(lambda x: 'ALTO POTENCIAL' if x == cluster_oro else 'BAJO POTENCIAL')

    print("\nResumen de Clusters Encontrados:")
    print(df.groupby('Potencial')['Barrio'].count())
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/barrios_bogota.csv', index=False)

    print("\nGenerando Mapa Interactivo...")
    mapa = folium.Map(location=[lat_center, lon_center], zoom_start=12)
    
    for idx, row in df.iterrows():
        color = 'green' if row['Potencial'] == 'ALTO POTENCIAL' else 'red'
        folium.Marker(
            [row['Latitud'], row['Longitud']],
            popup=f"{row['Barrio']}<br>Flujo: {row['Flujo_Peatonal']}<br>Arriendo: {row['Costo_Arriendo_Millones']:.1f}M",
            icon=folium.Icon(color=color, icon='store', prefix='fa')
        ).add_to(mapa)
        
    mapa.save('mapa_geomarketing.html')
    print("Mapa guardado en: mapa_geomarketing.html")

if __name__ == "__main__":
    analizar_geografia()
