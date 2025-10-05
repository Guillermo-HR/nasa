from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from sub_agents.data_analyst.agent_gcp import data_analyst_gcp
from sub_agents.visualizer.agent_gcp import visualizer_gcp

# --- Parche dentro del módulo: asegura vertexai antes del import ---
import sys, subprocess, importlib
try:
    importlib.import_module("vertexai")
except ModuleNotFoundError:
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "google-cloud-aiplatform>=1.70.0,<2.0.0"
    ])
    importlib.invalidate_caches()
# --- Fin parche ---

from vertexai.preview.generative_models import GenerativeModel

# ... el resto de tu código (función orquestador, etc.) ...

# 🔹 Agente orquestador principal (Manager)
root_agent = Agent(
    name="orquestador",
    model="gemini-2.0-flash",
    description="Orquesta el análisis y la visualización de datos urbanos desde CSV usando Vertex AI (Gemini).",
    instruction="""
    Eres un agente orquestador.
    - Si la solicitud incluye 'gráfica', 'grafica', 'correlación' o 'dispersión', delega al subagente visualizer.
    - En caso contrario, delega al subagente data_analyst.
    - Asegúrate de pasar 'file_path' y 'question' a los subagentes.
    Responde siempre con un lenguaje técnico y claro.
    """,
    sub_agents=[data_analyst_gcp, visualizer_gcp],
)


# 🔸 Wrapper para mantener compatibilidad con el frontend Streamlit
def orquestador(question: str, file_path: str):
    """
    Ejecuta la pregunta sobre el CSV utilizando Vertex AI (Gemini).
    Usa .complete() en lugar de .run() o .predict().
    """
    try:
        response = root_agent.complete(
            input=question,
            context={"file_path": file_path, "question": question}
        )

        # Devuelve solo el texto del modelo, no el objeto Response
        if hasattr(response, "output_text"):
            return response.output_text
        elif isinstance(response, str):
            return response
        else:
            return str(response)

    except Exception as e:
        return f"⚠️ Error al ejecutar el agente en GCP: {e}"
