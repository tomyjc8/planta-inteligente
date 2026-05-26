import random 

def generar_datos():
    datos = {
        "temperatura": random.randint(50, 100),
        "vibracion": round(random.uniform(0.1,3.0),2),
        "rpm": random.randint(1200, 1800)
    }
    return datos
