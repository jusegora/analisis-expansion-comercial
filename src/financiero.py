def calcular(nombre, flujo, arriendo_m):
    capex = 330.0 # Millones
    
    ticket = 25000
    conv = 0.05
    ventas = flujo * conv * ticket * 30
    margen = ventas * 0.35
    
    opex = (arriendo_m * 1_000_000) + 20_000_000
    
    utilidad = margen - opex
    
    if utilidad > 0:
        payback = (capex * 1_000_000) / utilidad
        roi = (utilidad * 12 / (capex * 1_000_000)) * 100
        print(f"{nombre}: Payback {payback:.1f} meses | ROI {roi:.1f}%")
    else:
        print(f"{nombre}: No viable.")

if __name__ == "__main__":
    calcular("Local A", 8000, 20.0)
    calcular("Local B", 12000, 35.0)
    calcular("Local C", 3000, 15.0)
