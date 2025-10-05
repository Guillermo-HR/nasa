"""
Agente local de visualización de datos.
Usa pandas y matplotlib para crear gráficos a partir de un CSV.
"""

from sub_agents.visualizer.tools import create_chart

def visualizer(question: str, file_path: str):
    """
    Simula el comportamiento del agente de visualización del ADK.
    Decide el tipo de gráfica y la genera según la pregunta.
    """
    try:
        return create_chart(file_path, question)
    except Exception as e:
        return f"⚠️ Error al generar la gráfica: {e}"
