import streamlit as st
import pandas as pd
import time
from sensores import generar_planta
from logger import guardar_datos

st.set_page_config(
    page_title="Planta Inteligente",
    layout="wide"
)

st.title("sistema inteligente de monitoreo industrial")

placeholder = st.empty()

while True:
    with placeholder.container():
        planta = generar_planta()

        guardar_datos(planta)

        for maquina in planta:
            st.subheader(maquina["nombre"])

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Temperatura",
                f"{maquina['temperatura']} °C"
                )
            
            col2.metric(
                "Vibración",
                maquina['vibracion']
                )
            
            col3.metric(
                "RPM",
                maquina['rpm']
                )

            col4.metric(
                "Estado",
                maquina['estado']
                )

            #alertas
            if maquina["temperatura"] > 85:
                st.error(f"{maquina['nombre']} está sobrecalentada!"
                )

            elif maquina["vibracion"] > 2.0:
                st.warning(f"{maquina['nombre']} tiene vibración excesiva!"
                )

            else:
                st.success(f"{maquina['nombre']} está funcionando normalmente."
                )
            
            #datos graficos
            df = pd.DataFrame({
                "temperatura": [maquina["temperatura"]],
                "vibracion": [maquina["vibracion"]],
                "rpm": [maquina["rpm"]]
            })

            st.line_chart(df)

            st.divider()
    time.sleep(2)
