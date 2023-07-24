from menu import runMainMenu
from user_registration import startUserRegistration
from user_authentication import login


def start():
    menuOption = runMainMenu()

    if menuOption == 1:
        startUserRegistration()
    elif menuOption == 2:
        login()
    elif menuOption == 3:
        # Eliminar cuando ya esté listo:
        print(">>> Opción no disponible aún. Regresando al menú principal...")
        start()
    elif menuOption == 4:
        print(">>> Saliendo al menú principal...")
        start()


start()
