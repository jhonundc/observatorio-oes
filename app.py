
import sqlite3
from pathlib import Path
import pandas as pd
import streamlit as st

DB = Path(__file__).with_name("oes.db")

st.set_page_config(page_title="OES académico", layout="wide")
st.title("Observatorio de Educación Superior — Prototipo académico")
st.caption("Registros didácticos; confirmar fuentes antes de uso institucional")

with sqlite3.connect(DB) as con:
    df = pd.read_sql_query(
        "SELECT * FROM noticias ORDER BY fecha DESC", con
    )

if df.empty:
    st.warning("No hay noticias. Ejecute preparar_datos.py")
    st.stop()

categorias = sorted(df["categoria"].unique().tolist())
seleccion = st.sidebar.multiselect(
    "Categoría", categorias, default=categorias
)
busqueda = st.sidebar.text_input("Buscar título o institución")

filtrado = df[df["categoria"].isin(seleccion)].copy()

if busqueda.strip():
    patron = busqueda.strip()
    mascara = (
        filtrado["titulo"].str.contains(
            patron, case=False, regex=False
        )
        | filtrado["institucion"].str.contains(
            patron, case=False, regex=False
        )
    )
    filtrado = filtrado[mascara]

c1, c2, c3 = st.columns(3)
c1.metric("Noticias", len(filtrado))
c2.metric("Instituciones", filtrado["institucion"].nunique())
c3.metric("Categorías", filtrado["categoria"].nunique())

st.subheader("Distribución por categoría")

if not filtrado.empty:
    st.bar_chart(filtrado["categoria"].value_counts())
else:
    st.info("No hay resultados con esos filtros")

st.subheader("Noticias registradas")
st.dataframe(
    filtrado[
        ["fecha", "institucion", "categoria", "titulo", "fuente", "url"]
    ],
    use_container_width=True,
    hide_index=True
)

st.download_button(
    "Exportar CSV",
    data=filtrado.to_csv(index=False).encode("utf-8-sig"),
    file_name="oes_resultados.csv",
    mime="text/csv"
)
