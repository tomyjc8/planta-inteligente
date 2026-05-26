import random 

def generar_motor(nombre):
    
        temperatura =random.randint(50, 100)
        vibracion = round(random.uniform(0.1,3.0),2)
        rpm = random.randint(1200, 1800)

        estado = "normal"

        if temperatura > 85:
            estado = "sobrecalentamiento"
        elif vibracion > 2.0:
            estado = "vibracion elevada"

        return {
            "nombre": nombre,
            "temperatura": temperatura,
            "vibracion": vibracion,
            "rpm": rpm,
            "estado": estado
        }

def generar_planta():
    
    planta = [
         generar_motor("Motor 1"),
         generar_motor("Motor 2"),
         generar_motor("bomba 1"),
         generar_motor("cinta transportadora")
    ]

    return planta
    
        

    
    
