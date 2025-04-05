# main.py
# Importamos nuestras funciones desde los módulos locales
import utils
import juego
def main():
# Mostramos mensaje de bienvenida (función en utils)
utils.mostrar_bienvenida()
# Llamamos a la función principal del juego (definida en juego.py)
juego.jugar()
# Mostramos mensaje de despedida (función en juego.py)
juego.despedida()
# Ejecutamos la función principal solo si este archivo es el principal
if __name__ == "__main__":
main()
