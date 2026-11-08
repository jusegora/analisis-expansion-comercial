import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import folium
import os

def analizar_ubicaciones():
    np.random.seed(42)
    n = 50
    
    flujo = np.random.randint(1000, 15000, n)
    estrato = np.random.choice([1, 2, 3, 4], n)
    arriendo = (flujo * 0.05) + (estrato * 2) + np.random.normal(0, 5, n)
    
    lat, lon = 4.59, -74.14
    
    df = pd.DataFrame({
        'barrio': [f"Barrio {i}" for i in range(1, n + 1)],
        'flujo': flujo,
        'estrato': estrato,
        'arriendo': arriendo
    })

    X = df[['flujo', 'estrato', 'arriendo']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    resumen = df.groupby('cluster').mean()
    mejor_cluster = resumen['flujo'].idxmax()
    
    df['potencial'] = df['cluster'].apply(lambda x: 'ALTO' if x == mejor_cluster else 'BAJO')

    print(df['potencial'].value_counts())
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/barrios.csv', index=False)

    mapa = folium.Map(location=[lat, lon], zoom_start=12)
    for _, row in df.iterrows():
        color = 'green' if row['potencial'] == 'ALTO' else 'red'
        folium.Marker(
            [lat + np.random.normal(0, 0.01), lon + np.random.normal(0, 0.01)],
            popup=row['barrio'],
            icon=folium.Icon(color=color, icon='store', prefix='fa')
        ).add_to(mapa)
        
    mapa.save('mapa_ubicaciones.html')

if __name__ == "__main__":
    analizar_ubicaciones()
