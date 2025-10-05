import pandas as pd

def load_csv(file_path: str):
    """
    Carga un CSV y devuelve un DataFrame de pandas.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error al cargar el archivo CSV: {e}")
import pandas as pd

def load_csv(file_path: str):
    """
    Carga un CSV y devuelve un DataFrame de pandas.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error al cargar el archivo CSV: {e}")
