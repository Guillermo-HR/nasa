import pandas as pd
import ollama

def analyze_csv(file_path: str, question: str):
    df = pd.read_csv(file_path)
    summary = df.describe(include='all').to_string()

    prompt = f"""
    Eres un analista de datos. Tienes este resumen del CSV:
    {summary}

    Usa pandas mentalmente para responder de forma concisa:
    {question}
    """

    response = ollama.chat(model="gemma2:2b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
