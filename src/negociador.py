import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def negociar(prop, local, pedido, objetivo, roi):
    llm = Groq(api_key=os.getenv("GROQ_API_KEY"), timeout=15.0)
    
    prompt = f"Eres gerente de expansion. Escribe un correo a {prop} por el local {local}. Piden ${pedido}M, ofrecemos ${objetivo}M. Menciona que el ROI actual es {roi}% y que un precio mas alto lo hace inviable. Se breve."

    res = llm.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="openai/gpt-oss-20b",
        temperature=0.3
    )
    
    print("\n--- Correo ---")
    print(res.choices[0].message.content)
    print("--------------")
    
    ok = input("¿Enviar? (S/N): ").upper()
    if ok == "S":
        print("Enviado (simulacion).")

if __name__ == "__main__":
    negociar("Inversiones Sur", "Local 2", 35.0, 28.0, 372.7)
