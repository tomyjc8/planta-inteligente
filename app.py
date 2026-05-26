import streamlit as st
import pandas as pd
from sensores import generar_datos

st.set_page_config(page_title="Planta Inteligente")
st.title("sistema inteligente de monitoreo industrial")
st.write("Sistema industrial funcionando")

#obter datos
datos = generar_datos()

temperatura = datos["temperatura"]
vibracion = datos["vibracion"]
rpm = datos["rpm"]

#mostrar metricas
col1, col2, col3 = st.columns(3)

col1.metric("Temperatura (°C)", temperatura)
col2.metric("Vibración", vibracion)
col3.metric("RPM", rpm)

#alertas 
if temperatura > 85:
    st.error("Alerta: Sobrecalentamiento detectado!")

if vibracion > 2.0:
    st.warning("Alerta: Vibración elevada!")

#historial
df = pd.DataFrame({
    "temperatura": [temperatura],
    "vibracion": [vibracion],
    "rpm": [rpm]
})

st.line_chart(df)