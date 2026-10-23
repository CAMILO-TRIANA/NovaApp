
import streamlit as st
from lectura import leer_archivo, resumen

st.set_page_config(page_title="NovaApp · Hito 0", layout="wide")
st.title("NovaApp · Cargar datos")
st.caption("Hito 0 · programa mínimo: abre el paquete y muestra filas, columnas y nombres.")

archivo = st.file_uploader("Suba el archivo del paquete (CSV o XLSX con hoja «datos»)",
                           type=["csv", "xlsx"])

if archivo is None:
    st.info("Esperando archivo…")
    st.stop()

try:
    df = leer_archivo(archivo)
except Exception as error:                      
    st.error(f"No se pudo leer el archivo: {error}")
    st.stop()

r = resumen(df)
c1, c2 = st.columns(2)
c1.metric("Filas", f"{r['filas']:,}".replace(",", "."))
c2.metric("Columnas", r["columnas"])

st.subheader("Nombres de las columnas")
st.dataframe({"#": range(1, r["columnas"] + 1),
              "Columna": r["nombres"],
              "Tipo leído": [str(t) for t in df.dtypes]},
             hide_index=True, use_container_width=True)

st.subheader("Vista previa (primeras 5 filas)")
st.dataframe(df.head(), use_container_width=True)
