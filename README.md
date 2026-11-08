# Sistema Integral de Expansion Retail (SIER)

**Autor:** jusegora  
*Data Analyst & Retail Expansion Manager*

Este repositorio contiene el sistema que desarrollé para abordar de forma analítica y financiera el reto de la expansión física en el sector retail. El proyecto demuestra la aplicación de herramientas técnicas avanzadas para la toma de decisiones gerenciales.

---

## 🏗️ Fase 1: Geomarketing y Análisis de Ubicación (Machine Learning)
*   **Archivo:** `src/geomarketing.py`
*   **Descripción:** Implementación del algoritmo K-Means (Scikit-Learn) para procesar datos de 50 barrios (flujo peatonal, estrato y costo de arriendo) en la zona sur de Bogotá. Identifica automáticamente los "Clústeres de Oro" (zonas de alto potencial).
*   **Visualización:** Genera un mapa interactivo (`mapa_geomarketing.html`) usando Folium, con pines de colores para priorizar la prospección inmobiliaria.
*   **Habilidad clave:** *Geomarketing aplicado a la búsqueda de locales comerciales.*

## 🏗️ Fase 2: Modelo Financiero (Evaluación CAPEX y ROI)
*   **Archivo:** `src/financiero.py`
*   **Descripción:** Motor de evaluación financiera que calcula la inversión inicial (CAPEX), los costos operativos (OPEX), las ventas proyectadas y la utilidad neta. Determina el **Payback** (tiempo de recuperación) y el **ROI Anual** de cada local evaluado.
*   **Habilidad clave:** *Modelos financieros para evaluacion de CAPEX y ROI.*

## 🏗️ Fase 3: Agente IA de Negociación (Agentic AI & HITL)
*   **Archivo:** `src/negociador.py`
*   **Descripción:** Agente de Inteligencia Artificial (conectado a Groq/LLM) que recibe los datos financieros del local y redacta automáticamente un correo de contraoferta para el propietario. 
*   **Seguridad:** Incluye un mecanismo *Human-in-the-Loop* (HITL) que exige la aprobación explícita del Gerente antes de "enviar" la oferta.
*   **Habilidad clave:** *Alta capacidad de negociación asistida por datos.*

---
**Tecnologías:** Python, Scikit-Learn, Pandas, Folium, Groq API (LLMs), Git.
