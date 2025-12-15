import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Operativo", page_icon="📊", layout="wide")
st.title("📊 Dashboard de Activos - MineTech")

# Cargar y Limpiar Datos
try:
    df = pd.read_csv('minetech_data.csv')
    if 'Valor_Activo' in df.columns:
        df['Valor_Activo_USD'] = df['Valor_Activo'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)
except:
    st.error("Error cargando datos.")
    st.stop()

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Activos", len(df))
c2.metric("Riesgo Promedio", f"{df['Nivel_Riesgo'].mean():.1f}/10")
c3.metric("Valor Total (USD)", f"${df['Valor_Activo_USD'].sum()/1000000:.1f} M")
c4.metric("Activos Críticos", len(df[df['Estado'] == 'Crítico']))

st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)
with col1:
    fig_bar = px.bar(df, x='Zona', y='Nivel_Riesgo', color='Zona', title="Riesgo por Zona")
    st.plotly_chart(fig_bar, use_container_width=True)
with col2:
    fig_pie = px.pie(df, names='Estado', title="Estado de Maquinaria", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("📋 Detalle de Datos")
st.dataframe(df)