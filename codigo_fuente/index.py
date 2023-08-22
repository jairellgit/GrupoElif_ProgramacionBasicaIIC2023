from menu import runMainMenu
from user_registration import startUserRegistration
from user_authentication import login
from menu_conf_avanzada import advancedSettings


def start():
    menuOption = runMainMenu()

    if menuOption == 1:
        startUserRegistration()
    elif menuOption == 2:
        login()
    elif menuOption == 3:
        advancedSettings()
    elif menuOption == 4:
        print("\nSaliendo de DreamWorld Casino... ¡Gracias por jugar!\n")


start()
