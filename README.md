# Analisis de Expansion Retail

**Por:** jusegora | Abogado & AI Solutions Architect | LegalTech & Análisis Forense de Datos

Herramientas que desarrollé para automatizar la toma de decisiones en la expansión de tiendas. En lugar de elegir locales "a ojo", el sistema usa datos para determinar si una ubicación es rentable.

## ¿Qué incluye?
- **Geomarketing (`geomarketing.py`):** Toma datos de barrios y usa K-Means para agruparlos en zonas de alto o bajo potencial. Genera un mapa en HTML.
- **Modelo Financiero (`financiero.py`):** Calcula el CAPEX inicial, el margen esperado y el ROI. Advierte si un local es inviable.
- **Negociador IA (`negociador.py`):** Un bot conectado a Groq que toma los datos financieros y redacta un correo de contraoferta para el dueño del local.

## Tecnologias
- Python 3
- Pandas y Scikit-Learn
- Folium
- Groq API

## Como ejecutar
Solo ejecuta los scripts con Python. Los datos de prueba se generan automáticamente.
