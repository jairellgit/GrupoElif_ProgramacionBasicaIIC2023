from menu import runMainMenu
from user_registration import addRegistration


def start():
    menuOption = runMainMenu()

    if menuOption == 1:
        addRegistration()
    elif menuOption == 2:
        # Eliminar cuando ya esté listo:
        print(">>> Opción no disponible aún. Regresando al menú principal...")
        start() 
    elif menuOption == 3:
        # Eliminar cuando ya esté listo:
        print(">>> Opción no disponible aún. Regresando al menú principal...")
        start()
    elif menuOption == 4:
        print(">>> Saliendo al menú principal...")
        start()


start()
