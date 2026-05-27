contador = 0

# while contador < 5:  
#     print(f"Me voy a parar aviso número {contador}") # esto es un print formateado
#     contador += 1

# respuesta = ""

# while respuesta.lower() != "si":
#     respuesta = input("Escribe si para salir: ")
    
# print("Has salido")


confirmar = "no"

while confirmar.lower() != "si":
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = input("Edad: ")
    
    confirmar = input("¿Está todo correcto? (si/no): ")
    
    while confirmar.lower() != "si" and confirmar.lower() != "no":
        confirmar = input("Responde solo si o no: ")
        
print("Datos enviados correctamente")







