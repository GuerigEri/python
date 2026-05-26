
# Obtener datos ---

# edad = int(input("Escribe tu edad: "))

# print(edad + 5)

# Condicionales --- 

# if edad > 18 :
#     print("Eres mayor de edad")
# elif edad == 18:
#     print("Tienes 18 años")
# else:
#     print("No eres mayor de edad")

# nombre = "Harry"

# if nombre.upper() == "Harry":
#     print("Harry querido, no te había visto, 20 puntos para gryffindor")
# elif nombre == "Ron":
#     print("Y tu eres...")
# else:
#     print("Troll en las mazmorras")

edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar al concierto")
elif edad >= 18 and not tiene_entrada:
    print("Eres mayor, pero no puedes entrar")


