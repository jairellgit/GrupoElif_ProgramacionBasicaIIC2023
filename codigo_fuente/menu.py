def printMainMenu():
    print("\n♦♦♦ DreamWorld Casino ♦♦♦")
    print("1) Registro de usuario nuevo")
    print("2) DreamWorld Casino")
    print("3) Configuración Avanzada")
    print("4) Salir")


def getMenuOption():
    menuOption = int(input("\nIngrese una opción del menú: "))
    return menuOption


def isValidMenuOption(menuOption):
    return menuOption >= 1 and menuOption <= 4


def validateMenuOption(menuOption):
    if (not isValidMenuOption(menuOption)):
        print("\n>>> Opción inválida, intente nuevamente...")
        return runMainMenu()

    return menuOption


def runMainMenu():
    printMainMenu()
    menuOption = getMenuOption()
    return validateMenuOption(menuOption)
