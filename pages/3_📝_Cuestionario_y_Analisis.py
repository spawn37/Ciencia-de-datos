import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Encuesta y Análisis", page_icon="📝", layout="wide")

st.title("📝 Encuesta: Cultura de Datos")
st.markdown("Analizando la percepción del valor del dato en tiempo real.")

# --- ⚠️ TU ENLACE CSV AQUÍ ---
ruta_google_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRKP0h7uVxy0hBy71cidt6-GYYoJUFeCMF3kXfBLABFFpthoonuVLdnpUXBoG5p14CwY3BZqC6JqRop/pub?output=csv"
url_formulario = "https://docs.google.com/forms/d/e/1FAIpQLSfAbgTAQVA9-98CRdr_08sWgejW5PetocsqNCgPdJMjOn0TlA/viewform?usp=header"

# Botón para ir al Form
if st.button("✍️ Ir a responder la encuesta en Google Forms"):
    st.markdown(f"[Haz clic aquí para abrir el formulario]({url_formulario})", unsafe_allow_html=True)

# --- CARGA Y LIMPIEZA DE DATOS ---
try:
    df = pd.read_csv(ruta_google_sheet)
    
    # LÓGICA CORREGIDA:
    # Columna 0 = Marca temporal (Timestamp)
    # Columna 1 = Nombre (Texto) -> La guardamos pero no la renombramos como P...
    # Columnas 2 en adelante = Preguntas (Numéricas) -> Estas serán P1, P2...
    
    # 1. Identificamos las columnas de preguntas (saltamos las 2 primeras: Fecha y Nombre)
    cols_preguntas = df.columns[2:] 
    
    # 2. Creamos el diccionario para renombrar (P1, P2... P10)
    nuevos_nombres = {col: f"P{i+1}" for i, col in enumerate(cols_preguntas)}
    df.rename(columns=nuevos_nombres, inplace=True)
    
    # 3. Guardamos la columna de Nombre con un nombre fácil
    df.rename(columns={df.columns[1]: 'Nombre_Participante'}, inplace=True)

except:
    st.warning("⚠️ Esperando datos...")
    st.stop()

# --- DASHBOARD ---
if not df.empty:
    st.divider()
    
    # Filtramos solo las columnas que empiezan con 'P' (P1, P2...) para los cálculos
    cols_numericas = [c for c in df.columns if c.startswith('P')]
    
    # 1. KPIs
    total = len(df)
    promedio_global = df[cols_numericas].mean().mean()
    
    c1, c2 = st.columns(2)
    c1.metric("👥 Total Encuestados", total)
    c2.metric("⭐ Promedio General de Acuerdo", f"{promedio_global:.1f} / 5.0")

    st.markdown("### 📊 Resultados por Pregunta (P1 a P10)")
    
    # 2. Gráfico
    promedios = df[cols_numericas].mean().reset_index()
    promedios.columns = ['Pregunta', 'Promedio']
    
    # Ordenamos para que salga P1 arriba y P10 abajo (o viceversa)
    promedios = promedios.sort_values('Pregunta', ascending=False)
    
    fig = px.bar(promedios, x='Promedio', y='Pregunta', orientation='h',
                 title="Nivel de Acuerdo (1=Desacuerdo, 5=Acuerdo)",
                 range_x=[1, 5], text_auto='.1f',
                 color='Promedio', color_continuous_scale='Blues')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 3. Tabla
    with st.expander("Ver tabla detallada"):
        st.dataframe(df)