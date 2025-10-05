from google.adk.agents import Agent
from sub_agents.data_analyst.tools_gcp import analyze_csv


# 🔹 Definición del agente de análisis de datos
data_analyst_gcp = Agent(
    name="data_analyst_gcp",
    model="gemini-2.0-flash",
    description="Analista urbano de datos CSV usando Vertex AI (Gemini).",
    instruction="""
    Eres un analista urbano experto en desigualdad e infraestructura.
    Usa la herramienta analyze_csv(file_path, question) para obtener estadísticas
    sobre el dataset y redacta una interpretación profesional.
    Responde con precisión técnica, conectando los resultados con temas
    de empleo, educación, salud o inclusión social urbana.
    """,
    tools=[analyze_csv],
)


# 🔸 Wrapper opcional (permite ejecutarlo directamente desde el orquestador)
def analyze_with_gemini(question: str, file_path: str):
    """
    Ejecuta el subagente 'data_analyst_gcp' con el modelo Gemini.
    Usa .complete() (no .run / .predict) según el ADK moderno.
    """
    try:
        response = data_analyst_gcp.complete(
            input=question,
            context={"file_path": file_path, "question": question},
        )

        # Devuelve el texto limpio
        if hasattr(response, "output_text"):
            return response.output_text
        elif isinstance(response, str):
            return response
        else:
            return str(response)

    except Exception as e:
        return f"⚠️ Error en data_analyst_gcp: {e}"