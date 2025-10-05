"""
Agente local de análisis de datos.
Usa pandas para explorar CSV y Ollama (Gemma 2 o Llama 3) para interpretar la pregunta.
"""

from sub_agents.data_analyst.tools import analyze_csv

def data_analyst(question: str, file_path: str):
    """
    Simula el comportamiento de un 'Agent' del ADK, pero local.
    """
    return analyze_csv(file_path, question)
