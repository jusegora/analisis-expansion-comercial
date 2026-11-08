import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generar_contraoferta(propietario, local, arriendo_pedido, arriendo_objetivo, roi_calculado):
    print(f"\n{'='*60}")
    print(f"🤖 AGENTE IA DE NEGOCIACION: Preparando contraoferta para {propietario}")
    print(f"{'='*60}")
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("ERROR: Falta la GROQ_API_KEY en el archivo .env")
        return

    llm = Groq(api_key=api_key, timeout=15.0)

    prompt_sistema = """Eres un Gerente de Expansion Senior experto en negociacion inmobiliaria retail.
    Tu tono debe ser profesional, persuasivo y basado en datos. 
    Escribe un correo formal al propietario."""

    prompt_usuario = f"""
    Propietario: {propietario}
    Local: {local}
    Arriendo solicitado: ${arriendo_pedido} millones
    Arriendo objetivo: ${arriendo_objetivo} millones
    ROI proyectado con el arriendo solicitado: {roi_calculado}%
    
    Redacta un correo corto (maximo 150 palabras) proponiendo el arriendo objetivo. 
    Justifica la oferta mencionando que un arriendo mas alto reduce el ROI del proyecto y hace inviable la apertura, 
    mientras que un arriendo justo garantiza un inquilino solido a largo plazo (empresa retail reconocida).
    No inventes datos, usa solo los que te di.
    """

    print("Redactando correo de negociacion con IA...\n")
    respuesta = llm.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        model="openai/gpt-oss-20b",
        temperature=0.3
    )
    
    correo = respuesta.choices[0].message.content
    print("--- BORRADOR DE CORREO GENERADO POR LA IA ---")
    print(correo)
    print("-----------------------------------------------")
    
    # Mecanismo Human-in-the-Loop (HITL)
    print("\n[HUMAN-IN-THE-LOOP REQUERIDO]")
    aprobacion = input("¿Aprueba usted el envio de este correo al propietario? (SI/NO): ").strip().upper()
    
    if aprobacion == "SI":
        print("\n✅ CORREO APROBADO. Enviando a", propietario, "...")
        print("(Simulacion: El correo ha sido enviado exitosamente).")
    else:
        print("\n❌ ACCION CANCELADA POR EL GERENTE. El correo no fue enviado.")

if __name__ == "__main__":
    # Simulamos los datos del Local 2, donde el propietario pide 35M pero nuestro objetivo es 28M
    generar_contraoferta(
        propietario="Inversiones Sur S.A.S.",
        local="Local Comercial Barrio Sur 2",
        arriendo_pedido=35.0,
        arriendo_objetivo=28.0,
        roi_calculado=372.7
    )
