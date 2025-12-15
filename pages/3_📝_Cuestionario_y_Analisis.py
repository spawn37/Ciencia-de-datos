import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Cuestionario y Análisis", page_icon="📝", layout="wide")

st.title("📝 Evaluación y Análisis del Conocimiento")

tab1, tab2 = st.tabs(["✍️ Responder Examen", "📈 Dashboard de Resultados"])

# --- TAB 1: EL EXAMEN ---
with tab1:
    st.subheader("Test: El Dato como Activo")
    
    with st.form("examen_form"):
        p1 = st.radio("1. ¿Diferencia entre dato e información?", 
                     ["Sin diferencia", "Dato es materia prima, información tiene contexto", "Información son números"])
        
        p2 = st.radio("2. ¿Qué es Gobernanza de Datos?", 
                     ["Políticas de calidad y seguridad", "Un software antivirus", "Gobierno de internet"])
        
        p3 = st.radio("3. ¿Por qué el dato es un activo?", 
                     ["Porque ocupa espacio", "Porque genera valor económico al procesarse", "Porque es bonito"])
        
        p4 = st.selectbox("4. ¿Herramienta clave para visualización?", ["Word", "Excel 97", "Dashboards Dinámicos"])
        
        submitted = st.form_submit_button("Enviar Respuestas")
        
        if submitted:
            nota = 0
            if p1 == "Dato es materia prima, información tiene contexto": nota += 5
            if p2 == "Políticas de calidad y seguridad": nota += 5
            if p3 == "Porque genera valor económico al procesarse": nota += 5
            if p4 == "Dashboards Dinámicos": nota += 5
            
            if nota == 20:
                st.success(f"¡Excelente! Nota: {nota}/20. Dominas el tema.")
                st.balloons()
            else:
                st.warning(f"Tu nota es: {nota}/20. Revisa el Dashboard de Resultados para ver estadísticas.")

# --- TAB 2: EL DASHBOARD DEL CUESTIONARIO ---
with tab2:
    st.subheader("📊 Análisis de Resultados del Grupo MineTech")
    st.markdown("Este dashboard analiza el rendimiento de **50 estudiantes** que ya tomaron la prueba.")
    
    # Simulación de datos de resultados (Mock Data)
    data_resultados = pd.DataFrame({
        'Estudiante': [f'Est-{i}' for i in range(50)],
        'Nota': np.random.randint(10, 21, 50), # Notas entre 10 y 20
        'Tiempo_minutos': np.random.randint(5, 15, 50),
        'Pregunta_Mas_Dificil': np.random.choice(['Definición Dato', 'Gobernanza', 'KPIs', 'Big Data'], 50)
    })
    
    # KPIs del Examen
    colA, colB, colC = st.columns(3)
    colA.metric("Promedio del Aula", f"{data_resultados['Nota'].mean():.1f}/20")
    colB.metric("Tasa de Aprobación", f"{len(data_resultados[data_resultados['Nota']>=14]) / 50 * 100:.0f}%")
    colC.metric("Tiempo Promedio", "8.5 min")
    
    # Gráficos
    c1, c2 = st.columns(2)
    with c1:
        fig_hist = px.histogram(data_resultados, x="Nota", nbins=5, title="Distribución de Notas", color_discrete_sequence=['#00CC96'])
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with c2:
        fig_pie = px.pie(data_resultados, names='Pregunta_Mas_Dificil', title="Temas con mayor dificultad")
        st.plotly_chart(fig_pie, use_container_width=True)