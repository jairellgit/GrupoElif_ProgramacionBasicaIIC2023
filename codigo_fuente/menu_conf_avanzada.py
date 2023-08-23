import os
import getpass
import helpers


config_file = "configuracion_avanzada.txt"
arrayConfAvanzada = helpers.confAvanzada()


# Función para eliminar un usuario y su información
def deleteUser(id):
    userFolder = f"users/{id}"
    
    if os.path.exists(userFolder):
        # Eliminar archivos y subcarpetas dentro de la carpeta del usuario
        for item in os.listdir(userFolder):
            item_path = os.path.join(userFolder, item)
            if os.path.isdir(item_path):
                try:
                    os.rmdir(item_path)
                except Exception as error:
                    print(f"Error al eliminar la carpeta {item_path}: {error}")
            else:
                try:
                    os.remove(item_path)
                except Exception as error:
                    print(f"Error al eliminar el archivo {item_path}: {error}")
        
        # Eliminar carpeta del usuario
        try:
            os.rmdir(userFolder)
        except Exception as error:
            print(f"Error al eliminar la carpeta del usuario {id}: {error}")
        
        # Eliminar información del usuario en usuarios_pines.txt
        linesSafe = []
        with open("usuarios_pines.txt", "r") as file:
            lines = file.readlines() # Lee todas las líneas del archivo y las almacena en la lista "lines"
            skip_user = False
            for line in lines:
                if skip_user:  # Saltar líneas asociadas al usuario a eliminar
                    skip_user = False
                    continue
                if line.strip() == id:  # Verifica si la línea actual contiene el ID que se desea eliminar
                    skip_user = True  # Indicar que las próximas líneas deben ser saltadas
                else:
                    linesSafe.append(line) # Si no es el ID a eliminar, agregar la línea a "linesSafe"

        with open("usuarios_pines.txt", "w") as file: # Abre el archivo "usuarios_pines.txt" para sobrescribir su contenido
            for line in linesSafe:
                file.write(line) # Escribe cada línea en el archivo, reemplazando el contenido original
        
        print(f">>> La información del usuario {id} ha sido eliminada exitosamente.")
    else:
        print(f">>> El usuario {id} no existe.")


def modifySystemValues():
    print("Valores actuales:")
    for index, value in enumerate(arrayConfAvanzada):
        print(f"{index + 1}. {value}")

    try:
        option = int(input("\nSeleccione el número de la opción que desea modificar: "))
        if 1 <= option <= len(arrayConfAvanzada):
            new_value = input(f"Ingrese el nuevo valor para '{arrayConfAvanzada[option - 1]}': ")
            arrayConfAvanzada[option - 1] = new_value

            with open(config_file, "w") as file:
                for value in arrayConfAvanzada:
                    file.write(f"{value}\n")

            print(">>> Valor modificado exitosamente.")
        else:
            print(">>> Opción inválida.")
    except ValueError:
        print(">>> Ingrese un número válido.")


# Función para acceder a la configuración avanzada
def advancedSettings():

    # Leer el PIN especial de la primera línea del archivo
    with open("usuarios_pines.txt", "r") as file:
        confPIN = file.readline().strip()

    # Solicitar el PIN al usuario
    inputPIN = getpass.getpass("Ingrese el PIN especial: \n> ")

    if inputPIN == confPIN:
        print(">>> Acceso a la configuración avanzada concedido.")
        while True:
            print("\nMenú de Configuración Avanzada:")
            print("1. Eliminar Usuario")
            print("2. Modificar Valores del Sistema")
            print("3. Salir")
            
            choice = int(input("\nSeleccione una opción: \n> "))

            if choice == 1:
                userIdDelete = input("Ingrese el ID del usuario que desea eliminar: \n> ")
                deleteUser(userIdDelete)
            elif choice == 2:
                print("\nMenú de Modificación de Valores del Sistema:")
                print(f"1. Valor mínimo depósito inicial (Actualmente {arrayConfAvanzada[0]})")
                print(f"2. Tipo de cambio: valor del colon (Actualmente {arrayConfAvanzada[1]})")
                print(f"3. Tipo de cambio: valor del bitcoin (Actualmente {arrayConfAvanzada[2]})")
                print(f"4. Acumulado del tragamonedas (Actualmente {arrayConfAvanzada[3]})")
                print(f"5. Apuesta mínima tragamonedas (Actualmente {arrayConfAvanzada[4]})")
                print(f"6. Apuesta mínima blackjack (Actualmente {arrayConfAvanzada[5]})")
                
                try:
                    choiceMenu2 = int(input("\nSeleccione una opción a modificar: "))
                    
                    if choiceMenu2 == 1:
                        arrayConfAvanzada[0] = input("Ingrese el nuevo valor mínimo del depósito inicial: \n> $")
                        print(">>> Valor modificado exitosamente.")
                    elif choiceMenu2 == 2:
                        arrayConfAvanzada[1] = input("Ingrese el nuevo valor para el 'Tipo de cambio: valor del colon': \n> $")
                        print(">>> Valor modificado exitosamente.")
                    elif choiceMenu2 == 3:
                        arrayConfAvanzada[2] = input("Ingrese el nuevo valor para el 'Tipo de cambio: valor del bitcoin': \n> $")
                        print(">>> Valor modificado exitosamente.")
                    elif choiceMenu2 == 4:
                        arrayConfAvanzada[3] = input("Ingrese el nuevo valor para el 'Acumulado del tragamonedas': \n> $")
                        print(">>> Valor modificado exitosamente.")
                    elif choiceMenu2 == 5:
                        arrayConfAvanzada[4] = input("Ingrese el nuevo valor para la 'Apuesta mínima del tragamonedas': \n> $")
                        print(">>> Valor modificado exitosamente.")
                    elif choiceMenu2 == 6:
                        arrayConfAvanzada[5] = input("Ingrese el nuevo valor para la 'Apuesta mínima del blackjack': \n> $")
                        print(">>> Valor modificado exitosamente.")
                    else:
                        print(">>> Opción no válida.")

                    with open(config_file, "w") as file:
                        for value in arrayConfAvanzada:
                            file.write(f"{value}\n")
                except Exception:
                    print("Solo puede ingresar números. Inténtelo nuevamente.")

            elif choice == 3:
                print(">>> Saliendo de la configuración avanzada...")
                helpers.returnToMainMenu()
            else:
                print(">>> Opción no válida. Inténtelo nuevamente.")
    else:
        print(">>> PIN especial incorrecto. Volviendo al menú principal...")
        helpers.returnToMainMenu()
