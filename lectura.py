
import pandas as pd

TIPOS_TEXTO = {"version_app": str, "id_sesion": str, "id_usuario": str}


def leer_archivo(archivo, nombre=None):
    """Lee un CSV (UTF-8, coma, punto decimal) o un XLSX con hoja «datos»."""
    nombre = (nombre or getattr(archivo, "name", "")).lower()
    if nombre.endswith(".csv"):
        return pd.read_csv(archivo, encoding="utf-8", sep=",", decimal=".",
                           dtype=TIPOS_TEXTO)
    if nombre.endswith(".xlsx"):
        return pd.read_excel(archivo, sheet_name="datos", dtype=TIPOS_TEXTO)
    raise ValueError("Formato no admitido: use un archivo .csv o .xlsx")


def resumen(df):
    """Filas, columnas y nombres, calculados a partir del archivo cargado."""
    return {"filas": len(df), "columnas": df.shape[1], "nombres": list(df.columns)}
