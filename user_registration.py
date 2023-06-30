userIdAttempts = 0


def validateUserIdAttempts():
    totalUserIdValidAttempts = 3
    global userIdAttempts
    userIdAttempts += 1

    if (userIdAttempts == totalUserIdValidAttempts):
        print(
            f"\nHa excedido el máximo de {totalUserIdValidAttempts} intentos para ingresar un ID válido, volviendo al menú principal...")

        # importante importar aquí y no al inicio para evitar una importación circular entre ambos módulos
        from index import start
        start()
    else:
        addRegistration()

# def isUserExists(userId):
    # Esta función booleana valida si un usuario existe o no


def isValidUserId(userId):
    MIN_USERID_LENGHT = 5
    return len(userId) >= MIN_USERID_LENGHT


def validateUserId(userId):
    if isValidUserId(userId):
        # if isUserExists(userId):
        #  print("\nEste userId ya es ocupado por otro usuario, intente nuevamente...")
        #  return validateUserIdAttempts()
        return userId

    print("\nId de usuario inválido, mínimo cinco caracteres...")
    validateUserIdAttempts()


def getUserId():
    print("Ingrese su ID (Alfanumérico), cinco caracteres mínimo")
    userId = input("> ")
    return validateUserId(userId)


def addRegistration():
    print("Registro de nuevo usuario")
    # punto 1
    userId = getUserId()
    print(f"id usuario: {userId}")  # línea de prueba, borrarla
    # punto 2
    userName = input("Ingrese su nombre: ")
