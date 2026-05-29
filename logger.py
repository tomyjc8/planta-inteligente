import pandas as pd
from datetime import datetime
import os

def guardar_datos(planta):

    registros = []

    for maquina in planta:

        registros.append({
            "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "maquina": maquina["nombre"],
            "temperatura": maquina["temperatura"],
            "vibracion": maquina["vibracion"],
            "rpm": maquina["rpm"],
            "estado": maquina["estado"]
        })
    df = pd.DataFrame(registros)

    archivo = "datos/historial.csv"

    if os.path.exists(archivo):
        df.to_csv(
            archivo,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            archivo,
            index=False
        )