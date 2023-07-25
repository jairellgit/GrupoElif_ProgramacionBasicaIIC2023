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
