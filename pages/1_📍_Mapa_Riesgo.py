import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

st.set_page_config(page_title="Mapa de Riesgos", page_icon="📍", layout="wide")

st.title("📍 Mapa de Riesgos Geoespacial")
st.markdown("Visualización satelital de zonas críticas en operación minera (Simulación Cerro Verde).")

# Cargar datos
try:
    df = pd.read_csv('minetech_data.csv')
except:
    st.error("No se encuentra minetech_data.csv")
    st.stop()

# Configurar Mapa
lat_prom = df['Latitud'].mean()
lon_prom = df['Longitud'].mean()

m = folium.Map(location=[lat_prom, lon_prom], zoom_start=14)
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri', name='Satélite'
).add_to(m)

# Mapa de Calor
heat_data = df[['Latitud', 'Longitud', 'Nivel_Riesgo']].values.tolist()
HeatMap(heat_data, radius=15, blur=20).add_to(m)

# Puntos Críticos
criticos = df[df['Estado'] == 'Crítico']
for i, row in criticos.iterrows():
    folium.Marker(
        [row['Latitud'], row['Longitud']],
        popup=f"ID: {row['ID_Activo']}\nRiesgo: {row['Nivel_Riesgo']}",
        icon=folium.Icon(color='red', icon='warning-sign')
    ).add_to(m)

# Mostrar en Streamlit
st_folium(m, width=1000, height=600)