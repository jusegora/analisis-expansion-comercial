import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generar_oferta(prop, local, pedido, objetivo, roi):
    llm = Groq(api_key=os.getenv("GROQ_API_KEY"), timeout=15.0)

    prompt = f"""
    Eres Gerente de Expansion. Escribe un correo a {prop} por el local {local}.
    Piden ${pedido}M, pero mi objetivo es ${objetivo}M.
    Usa el dato de que con el precio actual el ROI es de {roi}%.
    Se breve y profesional.
    """

    res = llm.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="openai/gpt-oss-20b",
        temperature=0.3
    )
    
    correo = res.choices[0].message.content
    print("\n--- Borrador de Correo ---")
    print(correo)
    print("--------------------------")
    
    ok = input("\n¿Enviar correo? (S/N): ").strip().upper()
    
    if ok == "S":
        print("Simulacion: Correo enviado exitosamente.")
    else:
        print("Accion cancelada.")

if __name__ == "__main__":
    generar_oferta("Inversiones Sur", "Local 2", 35.0, 28.0, 372.7)
