import pandas as pd

def evaluar_local(nombre, flujo_peatonal, costo_arriendo_millones):
    print(f"\n{'='*50}")
    print(f"EVALUACION FINANCIERA: {nombre}")
    print(f"{'='*50}")
    
    # 1. CAPEX (Inversion Inicial)
    adecuacion = 150.0 # Millones para adecuacion de local
    inventario_inicial = 100.0 # Millones
    equipos = 80.0 # Millones (neveras, estanterias, cajas)
    capex_total = adecuacion + inventario_inicial + equipos
    
    # 2. Proyeccion de Ingresos (Basado en flujo peatonal)
    # Supuesto: 5% del flujo entra, ticket promedio de $25,000, margen bruto 35%
    ticket_promedio = 25000
    tasa_conversion = 0.05
    ventas_mensuales = flujo_peatonal * tasa_conversion * ticket_promedio * 30 # 30 dias
    margen_bruto = ventas_mensuales * 0.35
    
    # 3. Costos Operativos Mensuales (OPEX)
    costo_arriendo = costo_arriendo_millones * 1_000_000 # Convertir a pesos
    nomina = 15.0 * 1_000_000 # 15 millones en nomina
    servicios = 5.0 * 1_000_000 # 5 millones en servicios
    opex_total = costo_arriendo + nomina + servicios
    
    # 4. Utilidad Neta Mensual
    utilidad_neta = margen_bruto - opex_total
    
    # 5. Metricas Financieras
    if utilidad_neta > 0:
        payback_meses = (capex_total * 1_000_000) / utilidad_neta
        roi_anual = (utilidad_neta * 12 / (capex_total * 1_000_000)) * 100
    else:
        payback_meses = float('inf')
        roi_anual = -100.0
    
    # 6. Impresion de Resultados
    print(f"CAPEX Total: ${capex_total:.1f} Millones")
    print(f"Ventas Mensuales Proyectadas: ${ventas_mensuales:,.0f}")
    print(f"Margen Bruto Mensual: ${margen_bruto:,.0f}")
    print(f"OPEX Mensual: ${opex_total:,.0f}")
    print(f"Utilidad Neta Mensual: ${utilidad_neta:,.0f}")
    print("-" * 50)
    if utilidad_neta > 0:
        print(f"PAYBACK: {payback_meses:.1f} meses")
        print(f"ROI ANUAL: {roi_anual:.1f}%")
    else:
        print("ALERTA: El local genera perdidas operativas. NO VIABLE.")
    print(f"{'='*50}")

if __name__ == "__main__":
    # Evaluamos 3 locales de ejemplo
    # Local A: Flujo 8,000 personas, Arriendo 20M
    evaluar_local("Local Comercial Barrio Sur 1", 8000, 20.0)
    
    # Local B: Flujo 12,000 personas, Arriendo 35M
    evaluar_local("Local Comercial Barrio Sur 2", 12000, 35.0)
    
    # Local C: Flujo 3,000 personas, Arriendo 15M
    evaluar_local("Local Comercial Barrio Sur 3", 3000, 15.0)
