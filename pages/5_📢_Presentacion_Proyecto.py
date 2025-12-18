import streamlit as st

st.set_page_config(page_title="Presentación del Proyecto", page_icon="📢", layout="wide")

# --- LÓGICA DE NAVEGACIÓN DE DIAPOSITIVAS ---
if 'slide' not in st.session_state:
    st.session_state.slide = 1

def next_slide():
    if st.session_state.slide < 8: # Cambia 8 por el número total de slides
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 1:
        st.session_state.slide -= 1

# --- BARRA SUPERIOR (Progreso y Botones) ---
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

# --- CONTENIDO DE LAS DIAPOSITIVAS ---
slide = st.session_state.slide

if slide == 1:
    st.header("1. Portada")
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", height=400)
    st.markdown("""
    ### **Tema: El Dato como Activo Estratégico**
    **Grupo:** MineTech  
    **Integrantes:**
    * Eduardo Ismael Trujillo Catacora
    * Aldair Alberto Yana Tamayo
    """)

elif slide == 2:
    st.header("2. Dato vs. Información")
    colA, colB = st.columns(2)
    with colA:
        st.info("📦 **Dato**")
        st.write("Es la materia prima sin procesar. Hechos aislados, números o caracteres.")
        st.code("Ejemplo: -16.409, 8, 'Tajo Norte'")
    with colB:
        st.success("🧠 **Información**")
        st.write("Son los datos procesados con contexto y propósito para tomar decisiones.")
        st.write("**Ejemplo:** 'El sensor del Tajo Norte indica riesgo crítico nivel 8.'")

elif slide == 3:
    st.header("3. ¿Por qué el dato es un activo?")
    st.markdown("""
    Al igual que una chancadora o un camión minero, **el dato tiene valor económico**.
    
    * **Genera Rentabilidad:** Al optimizar rutas y procesos.
    * **Evita Pérdidas:** Al predecir fallas en maquinaria (Mantenimiento Predictivo).
    * **Salva Vidas:** Al monitorear riesgos en tiempo real.
    
    > "Los datos son el nuevo petróleo, pero si no se refinan, no sirven para nada."
    """)

elif slide == 4:
    st.header("4. La Cadena de Valor del Dato")
    st.markdown("El proceso para transformar datos crudos en sabiduría de negocio:")
    st.graphviz_chart("""
        digraph {
            rankdir=LR;
            node [shape=box, style=filled, fillcolor="#e1f5fe"];
            Recoleccion -> Almacenamiento -> Procesamiento -> Analisis -> Decision;
        }
    """)
    st.write("1. **Recolección:** Sensores IoT, Formularios.")
    st.write("2. **Almacenamiento:** Bases de Datos, Nube.")
    st.write("3. **Análisis:** Dashboards, Algoritmos de IA.")
    st.write("4. **Decisión:** Acciones estratégicas.")

elif slide == 5:
    st.header("5. Gobernanza de Datos")
    st.warning("No basta con tener datos, hay que gobernarlos.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Principios Clave:**")
        st.markdown("* ✅ **Calidad:** Datos limpios y veraces.")
        st.markdown("* 🔒 **Seguridad:** Protección contra hackeos.")
        st.markdown("* ⚖️ **Ética:** Uso responsable y privacidad.")
    with col2:
        st.markdown("**Roles:**")
        st.markdown("* **CDO (Chief Data Officer):** Responsable de la estrategia.")
        st.markdown("* **Data Steward:** Custodio de la calidad diaria.")

elif slide == 6:
    st.header("6. Cultura Data-Driven")
    st.image("https://cdn-icons-png.flaticon.com/512/2620/2620986.png", width=150)
    st.markdown("""
    Una organización **Data-Driven** (impulsada por datos) no decide por "intuición" o "corazonadas".
    
    **Características:**
    * Democratización del acceso a la información.
    * Alfabetización de datos en todos los empleados.
    * Confianza en los algoritmos y métricas.
    """)

elif slide == 7:
    st.header("7. Caso Práctico: MineTech")
    st.markdown("""
    En este proyecto hemos aplicado estos conceptos:
    
    1. **Recolección:** Simulamos sensores en Cerro Verde.
    2. **Visualización:** Creamos un Mapa de Calor para identificar riesgos.
    3. **Valor:** El Dashboard financiero muestra millones de dólares en activos monitoreados.
    4. **Cultura:** El cuestionario evalúa la madurez digital del equipo.
    """)

elif slide == 8:
    st.header("8. Conclusiones")
    st.balloons()
    st.success("""
    * El dato es un activo **intangible** pero con impacto **financiero directo**.
    * La tecnología (Dashboards, IA) es el medio, pero la **cultura** es el motor.
    * Sin calidad y gobernanza, los datos se convierten en un pasivo (riesgo).
    """)

st.markdown("---")
# Botón para descargar (Opcional, solo visual si no tienes el archivo real)
st.caption("📥 Descargar presentación en formato PowerPoint (.pptx)")
# Si tuvieras el archivo real, descomenta la linea de abajo:
# with open("mi_presentacion.pptx", "rb") as file:
#     st.download_button("Descargar PPT", file, file_name="Presentacion_MineTech.pptx")