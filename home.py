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
    * **💰 Precios Metales:** Monitoreo financiero en vivo.
    """)
    st.info("💡 'Lo que no se mide, no se puede mejorar'.")

with col2:
    st.markdown("### 🏢 Minería 4.0")
    st.caption("Facultad de Ingeniería de Minas - VIII Semestre")

st.markdown("---")

# Sección Biografías
st.subheader("👥 Nuestro Equipo")
st.markdown("Estudiantes del VIII Semestre de la Facultad de Ingeniería de Minas.")

col_edu, col_ald = st.columns(2)

# --- BIOGRAFÍA DE EDUARDO ---
with col_edu:
    try:
        img_edu = Image.open("foto_eduardo.jpg")
        # Mostramos la imagen con borde redondeado (simulado) y ancho controlado
        st.image(img_edu, width=200)
    except:
        st.warning("Falta la foto 'foto_eduardo.jpg'")
    
    st.markdown("### Eduardo Ismael Trujillo Catacora")
    st.markdown("**Estudiante de Ingeniería de Minas (VIII Semestre)**")
    
    # Datos personales con iconos
    st.write("📍 **Origen:** Puno")
    st.write("🎂 **Nacimiento:** 13/11/2003")
    
    # Meta profesional en un recuadro de color
    st.success("🎯 **Meta Profesional:** Convertirse en Especialista en Ciencia de Datos aplicada a la minería.")

# --- BIOGRAFÍA DE ALDAIR ---
with col_ald:
    try:
        img_ald = Image.open("foto_aldair.jpg")
        st.image(img_ald, width=200)
    except:
        st.warning("Falta la foto 'foto_aldair.jpg'")
        
    st.markdown("### Aldair Alberto Yana Tamayo")
    st.markdown("**Estudiante de Ingeniería de Minas (VIII Semestre)**")
    
    # Datos personales
    st.write("📍 **Origen:** Juliaca")
    st.write("🎂 **Nacimiento:** 26/02/2003")
    
    # Meta profesional
    st.info("🎯 **Meta Profesional:** Convertirse en Analista de Riesgos y Sistemas en el sector extractivo.")

st.markdown("---")
st.caption("© 2025 MineTech - Proyecto de Ciencia de Datos")