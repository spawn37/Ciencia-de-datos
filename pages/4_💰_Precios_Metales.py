import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mercado de Metales", page_icon="💰", layout="wide")
st.title("💰 Precios de Minerales en Tiempo Real")
st.markdown("Monitoreo de Oro (Au), Plata (Ag) y Cobre (Cu) con conversión automática a Soles (PEN).")

# Función para cargar datos
def obtener_datos(ticker):
    # Descargamos historial de 1 año
    data = yf.Ticker(ticker).history(period="1y")
    return data

# Obtenemos la tasa de cambio USD -> PEN (Dólar a Soles)
try:
    tasa_pen = yf.Ticker("PEN=X").history(period="1d")['Close'].iloc[-1]
    st.success(f"💱 Tipo de Cambio Actual: **S/ {tasa_pen:.2f}**")
except:
    tasa_pen = 3.75 # Valor por defecto si falla la conexión
    st.warning("⚠️ No se pudo obtener el tipo de cambio. Usando valor ref: 3.75")

st.divider()

# Definimos los tickers (Símbolos de bolsa)
metales = {
    "Oro (Au)": "GC=F",    # Futuros de Oro
    "Plata (Ag)": "SI=F",  # Futuros de Plata
    "Cobre (Cu)": "HG=F"   # Futuros de Cobre
}

# Creamos pestañas para cada metal
tabs = st.tabs(metales.keys())

for i, (nombre, ticker) in enumerate(metales.items()):
    with tabs[i]:
        # Cargar data
        df = obtener_datos(ticker)
        
        # Calcular valores actuales
        precio_usd = df['Close'].iloc[-1]
        precio_pen = precio_usd * tasa_pen
        delta_dia = precio_usd - df['Close'].iloc[-2]
        
        # KPIs
        c1, c2, c3 = st.columns(3)
        c1.metric(f"Precio {nombre} (USD)", f"${precio_usd:,.2f}", f"{delta_dia:.2f}")
        c2.metric(f"Precio {nombre} (PEN)", f"S/ {precio_pen:,.2f}")
        c3.metric("Variación Diaria", f"{(delta_dia/precio_usd)*100:.2f}%")
        
        # Selección de moneda para el gráfico
        moneda = st.radio("Moneda del Gráfico:", ["USD ($)", "Soles (S/)"], key=ticker, horizontal=True)
        
        # Preparamos datos para graficar
        df_chart = df.reset_index()
        if moneda == "Soles (S/)":
            df_chart['Close'] = df_chart['Close'] * tasa_pen
            unit = "S/"
        else:
            unit = "$"
            
        # Gráfico de Línea
        fig = px.line(df_chart, x='Date', y='Close', title=f"Evolución del precio - {nombre}",
                      labels={'Close': f'Precio ({unit})', 'Date': 'Fecha'})
        
        # Color minero (Dorado para oro, gris plata, naranja cobre)
        color_linea = '#FFD700' if 'Oro' in nombre else ('#C0C0C0' if 'Plata' in nombre else '#B87333')
        fig.update_traces(line_color=color_linea)
        
        st.plotly_chart(fig, use_container_width=True)

st.caption("Fuente de datos: Yahoo Finance API (Retraso de 15 min en mercado gratuito).")