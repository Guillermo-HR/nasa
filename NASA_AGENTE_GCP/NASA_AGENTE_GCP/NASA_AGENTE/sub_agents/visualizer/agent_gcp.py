from google.adk.agents import Agent
from sub_agents.visualizer.tools_gcp import create_chart_gcp


# 🔹 Definición del agente visualizador
visualizer_gcp = Agent(
    name="visualizer_gcp",
    model="gemini-2.0-flash",
    description="Generador de gráficas e interpretaciones de datos urbanos (Vertex AI).",
    instruction="""
    Si el usuario solicita una gráfica:
    1. Llama a la herramienta create_chart_gcp(file_path, question) para generar la imagen.
    2. Analiza brevemente los patrones visuales (3-5 líneas):
       - Qué representa el gráfico.
       - Qué tendencia o relación se observa.
       - Qué implicaciones tiene en términos de desigualdad urbana, acceso o inclusión.
    3. Devuelve primero la RUTA de la imagen generada y luego la interpretación textual.
    """,
    tools=[create_chart_gcp],
)


# 🔸 Wrapper opcional para compatibilidad con el orquestador principal
def visualize_with_gemini(question: str, file_path: str):
    """
    Ejecuta el subagente 'visualizer_gcp' con Vertex AI (Gemini).
    Usa .complete() (no .run() / .predict()) según el ADK moderno.
    """
    try:
        response = visualizer_gcp.complete(
            input=question,
            context={"file_path": file_path, "question": question},
        )

        # Devuelve solo el texto del modelo o el string
        if hasattr(response, "output_text"):
            return response.output_text
        elif isinstance(response, str):
            return response
        else:
            return str(response)

    except Exception as e:
        return f"⚠️ Error en visualizer_gcp: {e}"