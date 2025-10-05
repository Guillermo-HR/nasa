import pandas as pd
import matplotlib.pyplot as plt
import os

def create_chart(file_path: str, question: str):
    """
    Genera una gráfica basada en la pregunta del usuario.
    Tipos admitidos: barras, dispersión.
    """
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) < 1:
        return "❌ No hay columnas numéricas para graficar."

    plt.figure(figsize=(8, 5))

    if "barras" in question.lower():
        df[numeric_cols].mean().plot(kind="bar", title="Promedio por columna")
    elif "dispersión" in question.lower() or "dispersion" in question.lower():
        if len(numeric_cols) >= 2:
            plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
            plt.xlabel(numeric_cols[0])
            plt.ylabel(numeric_cols[1])
            plt.title("Gráfica de dispersión")
        else:
            return " Se necesitan al menos dos columnas numéricas para una dispersión."
    else:
        return " No reconocí el tipo de gráfica. Usa 'barras' o 'dispersión'."

    output_path = "./data/grafica.png"
    plt.savefig(output_path)
    plt.close()

    return f"✅ Gráfica creada: {os.path.abspath(output_path)}"
