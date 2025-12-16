import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Encuesta y Análisis", page_icon="📝", layout="wide")

st.title("📝 Encuesta: Cultura de Datos")
st.markdown("Analizando la percepción del valor del dato en tiempo real.")

# --- ⚠️ AQUÍ PEGA TU LINK CSV DE GOOGLE SHEETS ---
# Recuerda: Archivo > Compartir > Publicar en la web > Formato CSV
ruta_google_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRKP0h7uVxy0hBy71cidt6-GYYoJUFeCMF3kXfBLABFFpthoonuVLdnpUXBoG5p14CwY3BZqC6JqRop/pub?output=csv"

# Link para que tus compañeros respondan
url_formulario = "https://docs.google.com/forms/d/e/1FAIpQLSfAbgTAQVA9-98CRdr_08sWgejW5PetocsqNCgPdJMjOn0TlA/viewform?usp=header"

# --- BOTÓN PARA IR AL FORMULARIO ---
st.info("📊 Este dashboard muestra estadísticas de opinión (Escala 1-5).")
if st.button("✍️ Ir a responder la encuesta en Google Forms"):
    st.markdown(f"[Haz clic aquí para abrir el formulario]({url_formulario})", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
try:
    df = pd.read_csv(ruta_google_sheet)
    
    # Renombrar columnas largas (P1, P2... etc)
    # Asumimos que la columna 0 es 'Marca temporal', empezamos desde la 1
    columnas_nuevas = {col: f"P{i}" for i, col in enumerate(df.columns) if i > 0}
    df.rename(columns=columnas_nuevas, inplace=True)

except:
    st.warning("⚠️ Aún no se han cargado datos o el enlace CSV no es correcto.")
    st.stop()

# --- DASHBOARD (SOLO SI HAY DATOS) ---
if not df.empty:
    st.divider()
    
    # 1. KPIs Simples
    total = len(df)
    # Calculamos el promedio de todas las columnas numéricas (las respuestas 1-5)
    cols_numericas = df.select_dtypes(include=['number']).columns
    promedio_global = df[cols_numericas].mean().mean()
    
    c1, c2 = st.columns(2)
    c1.metric("👥 Total Encuestados", total)
    c2.metric("⭐ Promedio General de Acuerdo", f"{promedio_global:.1f} / 5.0")

    st.markdown("### 📊 Resultados por Pregunta (Escala de Acuerdo)")
    
    # 2. Gráfico de Barras Horizontal
    # Calculamos el promedio de cada pregunta
    promedios_por_pregunta = df[cols_numericas].mean().reset_index()
    promedios_por_pregunta.columns = ['Pregunta', 'Promedio']
    
    # Graficamos
    fig = px.bar(promedios_por_pregunta, x='Promedio', y='Pregunta', orientation='h',
                 title="¿Qué tan de acuerdo están los encuestados? (1=Desacuerdo, 5=Acuerdo)",
                 range_x=[1, 5], text_auto='.1f',
                 color='Promedio', color_continuous_scale='Blues')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 3. Tabla de datos al final
    with st.expander("Ver tabla de respuestas completa"):
        st.dataframe(df)

else:
    st.info("Esperando la primera respuesta...")