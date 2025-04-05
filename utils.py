# utils.py
import random
def generar_numero_aleatorio(minimo, maximo): """ Retorna un número entero aleatorio entre 'minimo' y 'maximo'. """
return random.randint(minimo, maximo)
def mostrar_bienvenida():
""" Muestra un mensaje de bienvenida. """
print ("=======================================")
print (" ¡Bienvenido al juego de Adivina el Número! ")
print ("=======================================\n")