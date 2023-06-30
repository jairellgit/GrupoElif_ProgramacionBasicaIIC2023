from menu import runMainMenu
from user_registration import addRegistration


def start():
    menuOption = runMainMenu()

    if menuOption == 1:
        addRegistration()


start()
