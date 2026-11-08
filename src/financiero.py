def calc_roi(nombre, flujo, arriendo_m):
    capex = 150.0 + 100.0 + 80.0 # Adecuacion, inventario, equipos
    
    # Proyecciones
    ticket = 25000
    conv = 0.05
    ventas = flujo * conv * ticket * 30
    margen = ventas * 0.35
    
    # Costos
    opex = (arriendo_m * 1_000_000) + (15_000_000) + (5_000_000)
    
    utilidad = margen - opex
    
    if utilidad > 0:
        payback = (capex * 1_000_000) / utilidad
        roi = (utilidad * 12 / (capex * 1_000_000)) * 100
        print(f"{nombre}: CAPEX ${capex}M | Payback {payback:.1f} meses | ROI {roi:.1f}%")
    else:
        print(f"{nombre}: NO VIABLE (Perdida de ${utilidad:,.0f})")

if __name__ == "__main__":
    calc_roi("Local A", 8000, 20.0)
    calc_roi("Local B", 12000, 35.0)
    calc_roi("Local C", 3000, 15.0)
