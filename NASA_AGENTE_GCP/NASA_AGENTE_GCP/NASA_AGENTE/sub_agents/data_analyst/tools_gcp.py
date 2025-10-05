import pandas as pd

def analyze_csv(file_path: str, question: str) -> str:
    """
    Lee el CSV y retorna un resumen compacto que el agente Gemini
    usará como 'contexto factual' para razonar y responder en lenguaje natural.
    """
    df = pd.read_csv(file_path)

    shape = df.shape
    numeric = df.select_dtypes(include="number")
    num_cols = numeric.columns.tolist()

    # Resumen numérico acotado
    desc = numeric.describe().to_string()

    # Top 10 medias para no saturar el prompt
    means = numeric.mean().sort_values(ascending=False).head(10).to_string()

    # Muestra de columnas no numéricas
    non_num_cols = df.select_dtypes(exclude="number").columns.tolist()
    sample_non_num = {}
    for col in non_num_cols[:5]:
        sample_non_num[col] = df[col].dropna().astype(str).unique()[:5].tolist()

    context = (
        f"shape={shape}\n"
        f"numeric_columns={num_cols}\n\n"
        f"numeric_describe=\n{desc}\n\n"
        f"top10_means=\n{means}\n\n"
        f"sample_non_numeric_values={sample_non_num}\n"
    )

    # El agente (Gemini) usará este string para contestar la pregunta.
    return context
