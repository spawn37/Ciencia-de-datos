import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="MineTech - Home",
    page_icon="⛏️",
    layout="wide"
)

# Título Principal
st.title("⛏️ MineTech")
st.markdown("### El Dato como Activo de Valor para la Organización")
st.markdown("---")

# Sección Hero (Introducción)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Bienvenidos a la plataforma de demostración de **MineTech**. 
    Este proyecto de Ciencia de Datos explora cómo la información operativa puede transformarse en seguridad y rentabilidad.
    
    **Explora nuestras herramientas en el menú de la izquierda:**
    * **📍 Mapa de Riesgos:** Visualización geoespacial de activos.
    * **📊 Dashboard Operativo:** Análisis de KPIs en tiempo real.
    * **📝 Cuestionario:** Evaluación de conocimientos con análisis de resultados.
    """)
    st.info("💡 'Lo que no se mide, no se puede mejorar'.")

with col2:
    # Puedes poner una imagen de una mina o logo aquí si quieres
    st.markdown("### 🏢 Minería 4.0")

st.markdown("---")

# Sección Biografías
st.subheader("👥 Nuestro Equipo")

col_edu, col_ald = st.columns(2)

with col_edu:
    try:
        img_edu = Image.open("foto_eduardo.jpg")
        st.image(img_edu, width=200, caption="Eduardo Ismael Trujillo Catacora")
    except:
        st.warning("Falta la foto 'foto_eduardo.jpg'")
    
    st.markdown("**Eduardo Ismael Trujillo Catacora**")
    st.markdown("*Especialista en Ciencia de Datos*")
    st.caption("Encargado de la arquitectura de datos y modelamiento predictivo para la optimización de activos mineros.")

with col_ald:
    try:
        img_ald = Image.open("foto_aldair.jpg")
        st.image(img_ald, width=200, caption="Aldair Alberto Yana Tamayo")
    except:
        st.warning("Falta la foto 'foto_aldair.jpg'")
        
    st.markdown("**Aldair Alberto Yana Tamayo**")
    st.markdown("*Analista de Riesgos y Sistemas*")
    st.caption("Especialista en la implementación de dashboards operativos y estrategias de seguridad industrial.")

st.markdown("---")
st.caption("© 2025 MineTech - Proyecto de Ciencia de Datos")