import getpass
import helpers 

userIdAttempts = 0

userId = ""
userName = ""
userPin = 0 
userDeposit = 0

arrayTipoCambio = helpers.tipoDeCambio()

minMoneyDolar = float(arrayTipoCambio[0]) #El primer dato del archivo de Conf Avanzada es el monto mínimo de deposito requerido en dolares
minMoneyColon = float(arrayTipoCambio[1]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a colones
minMoneyBitcoin = float(arrayTipoCambio[2]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a bitcoins

def validateUserIdAttempts():
    totalUserIdValidAttempts = 3
    global userIdAttempts
    userIdAttempts += 1

    if (userIdAttempts == totalUserIdValidAttempts):
        print(
            f"\nHa excedido el máximo de {totalUserIdValidAttempts} intentos para ingresar un ID válido, volviendo al menú principal...")

        # importante importar aquí y no al inicio para evitar una importación circular entre ambos módulos
        helpers.returnToMainMenu()
    else:
        attemptsLeft = 3 - userIdAttempts
        print("\n>>> ID de usuario inválido, mínimo cinco caracteres. Le quedan "+str(attemptsLeft)+" intentos.") 
        addRegistration()
