# Analisis de Expansion Retail

**Por:** jusegora (Abogado y Cientifico de Datos)

Herramientas que desarrollé para automatizar la toma de decisiones en la expansión de tiendas. En lugar de elegir locales "a ojo", el sistema usa datos para determinar si una ubicación es rentable.

## ¿Qué incluye?

- **Geomarketing (`geomarketing.py`):** Toma datos simulados de barrios (flujo de gente, estrato, arriendo) y usa K-Means para agruparlos en zonas de alto o bajo potencial. Genera un mapa en HTML para verlo visualmente.
- **Modelo Financiero (`financiero.py`):** Un script rápido que calcula el CAPEX inicial, el margen esperado y el ROI. Si un local tiene mucho flujo pero el arriendo es muy caro, el script avisa que es inviable.
- **Negociador IA (`negociador.py`):** Un bot conectado a la API de Groq que toma los datos del análisis financiero y redacta un correo de contraoferta para el dueño del local, argumentando con números por qué el precio debe bajar.

## Tecnologias
- Python 3
- Pandas y Scikit-Learn (para el análisis de datos)
- Folium (para los mapas)
- Groq API (para la IA del negociador)

## Como ejecutar
Solo ejecuta los scripts con Python. Los datos de prueba se generan automáticamente.
