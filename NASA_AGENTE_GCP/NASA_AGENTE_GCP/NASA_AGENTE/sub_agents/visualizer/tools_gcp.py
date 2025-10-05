import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

COLUMN_LABELS = {
    "Abasto": "Acceso a abasto",
    "Cultura": "Acceso a cultura",
    "E_basica": "Educación básica",
    "E_media": "Educación media",
    "E_superior": "Educación superior",
    "Empleo": "Acceso a empleo formal",
    "Espacio_ab": "Espacio abierto (m² accesibles)",
    "Est_Tpte": "Transporte público masivo",
    "Pob_2010": "Población 2010",
    "Salud_cama": "Camas hospitalarias",
    "Salud_cons": "Consultorios de salud",
}

def create_chart_gcp(file_path: str, question: str) -> str:
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        return "❌ No hay columnas numéricas para graficar."

    os.makedirs("./data", exist_ok=True)
    output_path = "./data/grafica.png"

    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(10, 6))

    q = question.lower()
    if "barras" in q:
        mean_values = df[numeric_cols].mean().sort_values(ascending=False)
        mean_values.index = [COLUMN_LABELS.get(c, c) for c in mean_values.index]
        sns.barplot(x=mean_values.values, y=mean_values.index, palette="viridis")
        plt.title("Promedio de acceso por tipo de infraestructura urbana", fontsize=14)
        plt.xlabel("Promedio (normalizado)")
        plt.ylabel("")
    elif "dispersión" in q or "dispersion" in q:
        if len(numeric_cols) < 2:
            return "⚠️ Se necesitan al menos dos columnas numéricas para dispersión."
        x_col, y_col = numeric_cols[0], numeric_cols[1]
        sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.6)
        plt.title(f"Relación: {COLUMN_LABELS.get(x_col, x_col)} vs {COLUMN_LABELS.get(y_col, y_col)}", fontsize=14)
        plt.xlabel(COLUMN_LABELS.get(x_col, x_col))
        plt.ylabel(COLUMN_LABELS.get(y_col, y_col))
    elif "correlación" in q or "correlacion" in q:
        corr = df[numeric_cols].corr()
        sns.heatmap(corr, annot=False, cmap="coolwarm", cbar=True)
        plt.title("Mapa de correlación entre variables numéricas", fontsize=14)
    else:
        return "⚠️ Usa 'barras', 'dispersión' o 'correlación'."

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    return output_path  # devolvemos la ruta; el agente describirá con Gemini
