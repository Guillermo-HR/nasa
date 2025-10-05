# agent.py
from sub_agents.data_analyst.tools import analyze_csv
from sub_agents.visualizer.tools import create_chart
from tools.utils import load_csv

def orquestador(question: str, file_path: str):
    """
    Agente principal que decide si delegar el análisis o la visualización.
    """
    question_lower = question.lower()

    # Decide a quién delegar
    if "gráfica" in question_lower or "grafica" in question_lower:
        return create_chart(file_path, question)
    else:
        return analyze_csv(file_path, question)
