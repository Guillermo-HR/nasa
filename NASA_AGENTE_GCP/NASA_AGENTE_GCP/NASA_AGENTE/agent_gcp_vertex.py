from vertexai.preview.generative_models import GenerativeModel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import vertexai

# 🔹 Inicializa Vertex AI con tu proyecto y región
vertexai.init(project="airy-parsec-474204-e7", location="us-central1")

# Carga del modelo Gemini directamente desde Vertex AI
model = GenerativeModel("gemini-2.0-flash")

def analyze_csv(file_path: str, question: str) -> str:
    """Procesa el CSV y pide a Gemini un análisis directo."""
    df = pd.read_csv(file_path)
    numeric = df.select_dtypes(include="number")
    summary = numeric.describe().to_string()
    prompt = f"""
    Eres un analista urbano de datos. Analiza el siguiente resumen del dataset
    del Índice de Desigualdad Urbana y responde la pregunta del usuario.

    Pregunta: {question}

    Resumen estadístico:
    {summary}
    """
    response = model.generate_content(prompt)
    return response.text


def create_chart(file_path: str, question: str) -> str:
    """Genera una gráfica y pide a Gemini que la interprete."""
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    os.makedirs("./data", exist_ok=True)
    output_path = "./data/grafica.png"

    if "barras" in question.lower():
        mean_values = df[numeric_cols].mean().sort_values(ascending=False)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=mean_values.values, y=mean_values.index, palette="viridis")
        plt.title("Promedio de acceso por variable")
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()
    else:
        return "⚠️ Usa 'barras' para generar una gráfica."

    prompt = f"""
    Se generó una gráfica basada en los datos del Índice de Desigualdad Urbana de La Paz.
    Describe en 3-5 líneas qué muestra la gráfica y qué patrones o desigualdades observas.
    """
    response = model.generate_content(prompt)
    return f"{output_path}\n\n📊 Interpretación: {response.text}"


def orquestador(question: str, file_path: str):
    """Decide si generar gráfico o análisis según la pregunta."""
    if "gráfica" in question.lower() or "grafica" in question.lower():
        return create_chart(file_path, question)
    else:
        return analyze_csv(file_path, question)