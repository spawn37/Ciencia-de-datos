import streamlit as st
from PIL import Image # <-- AGREGAMOS ESTA IMPORTACIÓN

st.set_page_config(page_title="Presentación del Proyecto", page_icon="📢", layout="wide")

# --- LÓGICA DE NAVEGACIÓN ---
if 'slide' not in st.session_state:
    st.session_state.slide = 1

def next_slide():
    if st.session_state.slide < 8:
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 1:
        st.session_state.slide -= 1

# --- BARRA SUPERIOR ---
st.title("📢 El Dato como Activo de Valor")
progress = (st.session_state.slide / 8)
st.progress(progress)

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("⬅️ Anterior"):
        prev_slide()
with col3:
    if st.button("Siguiente ➡️"):
        next_slide()

st.markdown("---")

# --- CONTENIDO ---
slide = st.session_state.slide

# === CORRECCIÓN AQUÍ EN LA DIAPOSITIVA 1 ===
if slide == 1:
    st.header("1. Portada")
    try:
        # Intentamos abrir la imagen local
        img_portada = Image.open("portada_ppt.jpg")
        st.image(img_portada, caption="Minería a Gran Escala y Datos", use_container_width=True)
    except FileNotFoundError:
        # Si te olvidaste de guardar la foto, saldrá este aviso
        st.warning("⚠️ Falta el archivo 'portada_ppt.jpg' en la carpeta Minetech.")
        st.info("Por favor descarga una imagen de mina, guárdala con ese nombre y sube los cambios a GitHub.")
    
    st.markdown("""
    ### **Tema: El Dato como Activo Estratégico**
    **Grupo:** MineTech  
    **Integrantes:**
    * Eduardo Ismael Trujillo Catacora
    * Aldair Alberto Yana Tamayo
    """)
# ===========================================

elif slide == 2:
    st.header("2. Dato vs. Información")
    colA, colB = st.columns(2)
    with colA:
        st.info("📦 **Dato**")
        st.write("Es la materia prima sin procesar. Hechos aislados.")
        st.code("-16.409, 8, 'Tajo Norte'")
    with colB:
        st.success("🧠 **Información**")
        st.write("Datos procesados con contexto para tomar decisiones.")
        st.write("**Ejemplo:** 'Alerta crítica en Tajo Norte (Nivel 8).'")

elif slide == 3:
    st.header("3. ¿Por qué el dato es un activo?")
    st.markdown("""
    Al igual que la maquinaria amarilla, **el dato tiene valor financiero**:
    * **Rentabilidad:** Optimiza el consumo de combustible.
    * **Mantenimiento:** Predice fallas antes de que ocurran.
    * **Seguridad:** Monitorea taludes y evita accidentes.
    """)

elif slide == 4:
    st.header("4. La Cadena de Valor")
    st.graphviz_chart("""
        digraph {
            rankdir=LR;
            node [shape=box, style=filled, fillcolor="#e1f5fe"];
            Recoleccion -> Almacenamiento -> Procesamiento -> Analisis -> Decision;
        }
    """)

elif slide == 5:
    st.header("5. Gobernanza de Datos")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("✅ **Calidad:** Datos limpios y reales.")
        st.markdown("🔒 **Seguridad:** Protección contra accesos no autorizados.")
    with col2:
        st.markdown("⚖️ **Ética:** Privacidad de la información.")

elif slide == 6:
    st.header("6. Cultura Data-Driven")
    st.markdown("Decisiones basadas en **evidencia**, no en intuición.")
    st.metric(label="Confianza en Decisiones", value="95%", delta="Data-Driven")

elif slide == 7:
    st.header("7. Caso Práctico: MineTech")
    st.write("1. **Recolección:** Sensores simulados (GPS, Riesgo).")
    st.write("2. **Visualización:** Mapa de Calor y Dashboard Financiero.")
    st.write("3. **Decisión:** Alertas automáticas para activos críticos.")

elif slide == 8:
    st.header("8. Conclusiones")
    st.balloons()
    st.success("Sin calidad y gobernanza, los datos son un riesgo. Con gestión adecuada, son el activo más valioso.")