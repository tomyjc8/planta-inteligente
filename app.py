import streamlit as st
import pandas as pd
import time
import os
from sensores import generar_planta
from logger import guardar_datos


st.set_page_config(
    page_title="Planta Inteligente",
    layout="wide"
)

st.title("sistema inteligente de monitoreo industrial")

if os.path.exists("datos/historial.csv"):

    historial = pd.read_csv("datos/historial.csv")
    
    temp_promedio = round(historial["temperatura"].mean(), 1)
    vib_promedio = round(historial["vibracion"].mean(), 2)
    rpm_promedio = round(historial["rpm"].mean(), 0)

    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric(
        "Temperatura Promedio",
        f"{temp_promedio} °C"
    )

    kpi2.metric(
        "Vibración Promedio",
        vib_promedio
    )

    kpi3.metric(
        "RPM Promedio",
        rpm_promedio
    )

placeholder = st.empty()

while True:
    with placeholder.container():
        planta = generar_planta()

        tabla_planta = pd.DataFrame(planta)

        st.subheader("Estado General de la Planta")

        st.dataframe(
            tabla_planta,
            use_container_width=True
        )

        if os.path.exists("datos/historial.csv"):
            
            historial = pd.read_csv("datos/historial.csv")

            alarmas = len(
                historial[
                    (historial["estado"] != "normal")
                ]   
            )

            st.metric(
                "Alarmas Registradas",
                alarmas
            )
            
            st.subheader("Historico de Temperatura")

            st.line_chart(
                historial["temperatura"].tail(100)
            )
            st.subheader("Historico de Vibración")

            st.line_chart(
                historial["vibracion"].tail(100)
            )

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
