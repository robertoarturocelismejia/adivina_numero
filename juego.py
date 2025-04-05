# juego.py
# Importamos la función para generar números aleatorios desde utils
from utils import generar_numero_aleatorio
def jugar():
""" Función principal que ejecuta el juego de adivinar el número. """
print("Estoy pensando, y es en un número del 1 al 10. ¿Puedes adivinarlo?")
numero_secreto = generar_numero_aleatorio(1, 10)
intentos = 0
adivinado = False
while not adivinado:
# Pedimos al usuario que ingrese un número
respuesta = input("Ingresa tu número: ")
# Validamos que la respuesta sea un número
if not respuesta.isdigit():
print("Por favor, ingresa un valor numérico.")
continue
# Convertimos la respuesta a entero
numero_ingresado = int(respuesta)
intentos += 1
if numero_ingresado < numero_secreto:
print("Demasiado bajo, intenta de nuevo.\n")
elif numero_ingresado > numero_secreto:
print("Demasiado alto, intenta de nuevo.\n")
else:
print(f"¡Felicidades! Adivinaste el número en {intentos} intento(s).")
adivinado = True
def despedida():
""" Función para mostrar un mensaje de despedida. """
print("\nGracias por jugar. ¡Hasta la próxima!")
