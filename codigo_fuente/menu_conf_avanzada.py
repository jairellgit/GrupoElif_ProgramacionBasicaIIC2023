import os
import getpass
import helpers


config_file = "configuracion_avanzada.txt"
arrayConfAvanzada = helpers.confAvanzada()


def passwordAdvancedConf():
    filePinAdvanced = "usuarios_pines.txt"

    with open(filePinAdvanced, "r") as file:
        pinAdvanced = file.readline().strip()
    return pinAdvanced


# Función para autenticar como usuario avanzado
def authenticateAdvancedUser():
    pinAdvanced = passwordAdvancedConf()
    pin = getpass.getpass("Ingrese el PIN de usuario avanzado: ")

    if (pin == pinAdvanced):
        advancedConfigurationMenu()
    else:
        print("PIN incorrecto. Regresando al menú principal.")
        helpers.returnToMainMenu()


# Función para mostrar el menú de configuración avanzada
def advancedConfigurationMenu():
    while True:
        print("\nConfiguración Avanzada:")
        print("1. Eliminar usuario")
        print("2. Modificar valores del sistema")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            # deleteUser()
            print("Opción desactivada temporalmente")
        elif choice == "2":
            # modifySystemValues()
            print("Opción desactivada temporalmente")
        elif choice == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Función para eliminar un usuario
def deleteUser():
    inputUserId = input("Ingrese el ID del usuario que desea eliminar: ")
    userPath = f"users/{inputUserId}"

    if os.path.exists(userPath):
        confirm = input(
            f"¿Está seguro de eliminar al usuario '{inputUserId}'? \nDigite 'Si' para confirmar: ")
        if confirm.lower() == "Si":
            try:
                os.rmdir(userPath)  # Elimina la carpeta del usuario
                deleteUserFromCredentials(inputUserId)
                print(f"Usuario '{inputUserId}' eliminado correctamente.")
            except Exception as e:
                print("Error al eliminar el usuario:", e)
        else:
            print("Eliminación cancelada.")
    else:
        print(f"El usuario '{inputUserId}' no existe.")


# Función para eliminar un usuario del archivo 'usuarios_pines.txt'
def deleteUserFromCredentials(user_id):
    lines_safe = []
    with open("usuarios_pines.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            if lines[i].strip() != user_id:
                lines_safe.extend(lines[i:i+3])

    with open("usuarios_pines.txt", "w") as file:
        for line in lines_safe:
            file.write(line)


"""
# Función para modificar valores del sistema
def modifySystemValues():
    print("\nValores del Sistema:")
    for i in arrayConfAvanzada:
        print(f"{i}. ")

    try:
        choice = int(input("Seleccione el número del valor que desea modificar: ")) - 1
        if 0 <= choice < len(system_values):
            new_value = input(f"Ingrese el nuevo valor para '{system_values[choice][1]}': ")
            system_values[choice][0] = new_value
            writeSystemValues(config_file, system_values)
            print(f"Valor '{system_values[choice][1]}' actualizado correctamente.")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Ingrese un número válido.")
"""


# Función para escribir los valores del sistema en el archivo
def writeSystemValues(file_path, system_values):
    with open(file_path, "w") as file:
        for value, description in system_values:
            file.write(f"{value} - {description}\n")
