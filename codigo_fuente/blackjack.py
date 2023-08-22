import random
import helpers
import user_authentication
import menu_casino

userId = None
userPin = None
userName = None
amountToBet = 0
playerMoney = 0

arrayConfigAvanzada = helpers.confAvanzada()


def start(id, pin, name):
    resetGlobalValues(id, pin, name)
    showInstructions()

    amountToBetHandle()

    play()


def resetGlobalValues(id, pin, name):
    global playerCards
    global crupierCards
    global hasDividedCards
    global userId
    global userPin
    global userName
    global amountToBet
    global playerMoney

    playerCards = []
    crupierCards = []
    hasDividedCards = False
    userId = id
    userPin = pin
    userName = name
    amountToBet = 0
    playerMoney = menu_casino.getMoney(userId)


def showInstructions():
    global userName

    print(f"\n♦ ¡Bienvenido al Blackjack {userName}! ♦")
    print("Estas son las reglas del juego:")
    print("1. El objetivo es sumar los valores de las cartas para acercarse a 21, si se pasa de 21 pierde.")
    print("2. Las cartas con número valen ese número, las cartas J, Q, K valen 10, y el As puede valer 1 u 11, usted decide.")
    print("3. El crupier le dará dos cartas visibles, y él tendrá una carta visible y otra oculta.")
    print("4. Puede pedir carta nueva para ir sumando o decidir detenerse.")
    print("5. Para ganar debe sumar 21 con sus cartas o estar más cercano al 21 que el crupier.")
    print("6. Después de repartir las cartas, tiene la opción de doblar su apuesta.")
    print("7. Si obtiene una carta repetida, puede dividir y jugar con dos manos.")
    print("8. Existe el empate, y si usted o el crupier se pasan de 21 pierden.")


def amountToBetHandle():
    global amountToBet

    amountToBet = getAmountToBet()
    checkAmountToBet(amountToBet)


def getAmountToBet():
    amountToBet = getValidAmountFormat()

    return amountToBet


def getValidAmountFormat():
    amountToBet = 0

    while True:
        try:
            amountToBet = float(input("\nIngrese su apuesta: "))
            break
        except ValueError:
            print("\n>>> Sólo se admiten números.")

    return amountToBet


def checkAmountToBet(amountToBet):
    global arrayConfigAvanzada
    global userId
    global playerMoney

    minAmountToBet = float(arrayConfigAvanzada[5])

    print(f"\nSu saldo actual es de: ${playerMoney}")

    if minAmountToBet > playerMoney:
        print(
            f"\nNo tiene suficiente saldo... el mínimo es: ${minAmountToBet}")
        print("Volviendo al submenú de juegos...")
        user_authentication.menuCasino(userId, userPin, userName)

    if not hasPlayerEnoughMoney(amountToBet, playerMoney):
        print(
            f"\nNo puede apostar ${amountToBet}, ya que su saldo es de: ${playerMoney}")
        print("Porfavor reintente")
        amountToBetHandle()

    if amountToBet < minAmountToBet:
        print(
            f"\nNo puede apostar ${amountToBet}, ya que el mínimo son ${minAmountToBet}")
        print("Porfavor reintente")
        amountToBetHandle()


def hasPlayerEnoughMoney(amountToBet, playerMoney):
    return amountToBet <= playerMoney


def play():
    print("\n¡Comienza el juego!")
    assignCards()


playerCards = []
crupierCards = []


def assignCards():
    global playerCards
    global crupierCards
    global hasDividedCards

    print("El crupier reparte las cartas...\n")

    assignCardsTurns = 2
    for i in range(assignCardsTurns):
        playerCards.append(getRandomCard("player"))
        print(f"Te ha tocado un {playerCards[i]}")
        crupierCards.append(getRandomCard("crupier"))
        if i == 1:
            print(f"Al crupier le tocó un {crupierCards[i]}")
        else:
            print("La primer carta del crupier esta oculta.")

    askToDobuleBet()

    if (arePlayerCardsEqual(playerCards)):
        askToDivideCards()

    if not hasDividedCards:
        checkScore(playerCards)

    menu()


def getRandomCard(user):
    cardValues = ["As", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
    cardTypes = ["Corazones", "Rombos", "Tréboles", "Picas"]

    randomValue = random.randint(0, len(cardValues) - 1)
    cardValue = cardValues[randomValue]

    if (cardValue == "As" and user == "player"):
        cardValue = f"{getAsCardValue()} (As)"
    elif (cardValue == "As" and user == "crupier"):
        asValidValues = ["1", "11"]
        randomAsValidValue = random.randint(0, 1)
        cardValue = f"{asValidValues[randomAsValidValue]} (As)"

    randomType = random.randint(0, len(cardTypes) - 1)
    cardType = cardTypes[randomType]

    cardColor = None

    if ((cardType == "Corazones") or (cardType == "Rombos")):
        cardColor = "Rojo"
    elif ((cardType == "Tréboles") or (cardType == "Picas")):
        cardColor = "Negro"

    randomCard = f"{cardValue} de {cardType} {cardColor}"

    return randomCard


def getAsCardValue():
    print("\nObtuvo un 'As', elija el valor del As: ")
    print("1) Quiero que sea 1")
    print("2) Quiero que sea 11")

    while True:
        option = input(">>> ")

        if isValidAsCardOption(option):
            if option == "1":
                asCardValue = "1"
            else:
                asCardValue = "11"

            break

        print("\nValor del As inválido, reintente...")

    return asCardValue


def isValidAsCardOption(asCardOption):
    return (asCardOption == "1") or (asCardOption == "2")


def arePlayerCardsEqual(playerCards):
    values = getCardValues(playerCards)

    return values[0] == values[1]


def askToDobuleBet():
    print("\n¿Desea doblar su apuesta?")
    print("1) Sí")
    print("2) No")

    while True:
        option = input(">>> ")

        if option == "1" or option == "2":
            break
        else:
            print("\nOpción inválida, reintente...")

    if option == "1":
        doubleBet()


def doubleBet():
    global amountToBet
    global userId
    global playerMoney
    global arrayConfigAvanzada

    newAmountToBet = amountToBet * 2

    print(f"\nApuesta inicial: ${amountToBet}")
    print(f"Apuesta doblada: ${newAmountToBet}")
    print(f"Su saldo: ${playerMoney}")

    if not hasPlayerEnoughMoney(newAmountToBet, playerMoney):
        print("\nNo puede doblar, ya que la cantidad excede su saldo.")
        return

    amountToBet = newAmountToBet
    menu_casino.updateMoney(userId, newAmountToBet)


hasDividedCards = False


def askToDivideCards():
    global hasDividedCards

    print("\nObtuvo 2 cartas de igual valor, ¿Desea dividir en dos manos?")
    print("1) Sí")
    print("2) No")

    while True:
        option = input(">>> ")

        if isValidDivideCardsOption(option):
            break

        print("\nOpción inválida, reintente...")

    if option == "1":
        hasDividedCards = True
        divideCards()


def isValidDivideCardsOption(option):
    return option == "1" or option == "2"


def divideCards():
    global playerCards

    playerCards = [[playerCards[0]], [playerCards[1]]]


def checkScore(playerHand):
    playerScore = sum(getCardValues(playerHand))
    blackjack = 21

    if playerScore >= blackjack:
        checkBlackjack(playerHand)


def checkBlackjack(playerHand):
    global crupierCards
    global hasDividedCards
    global userId
    global playerMoney
    global amountToBet

    blackjack = 21
    crupierScore = sum(getCardValues(crupierCards))
    playerScore = sum(getCardValues(playerHand))

    print("\n♦ Resultados ♦")
    print(f"Tu puntuación es de {playerScore}")

    if (playerScore > blackjack):
        if hasDividedCards:
            print(
                f"\nPuntuación por encima de {blackjack}... Ha perdido una mano.")
            return removeHand(playerHand)

        print(
            f"\nPuntuación por encima de {blackjack}... Ha perdido su apuesta de ${amountToBet}.")

        newBalance = playerMoney - amountToBet
        menu_casino.updateMoney(userId, newBalance)
        stayPlayingOrReturn()

    print(f"La carta oculta del crupier es: {crupierCards[0]}")
    print(f"Y su segunda carta es: {crupierCards[1]}")

    while True:
        newCard = getRandomCard("crupier")
        crupierCards.append(newCard)
        print(f"\nEl crupier saca un {newCard}")

        lastCardValue = getCardValues(crupierCards)[-1]
        crupierScore += lastCardValue
        print(f"Puntuación del crupier: {crupierScore}")

        if crupierScore >= playerScore:
            if (playerScore == crupierScore):
                print("\n¡Es un empate! No ganas ni pierdes la apuesta.")

                if hasDividedCards:
                    print(
                        f"\nPerdiste esta mano, te queda la otra mano.")
                    return removeHand(playerHand)

                break

            elif (crupierScore > blackjack):
                print("\n¡Ganaste! El crupier se pasó de 21")
                print(f"Has ganado ${amountToBet * 2}")

                newBalance = playerMoney + (amountToBet * 2)
                menu_casino.updateMoney(userId, newBalance)

                break

            elif (crupierScore > playerScore):
                print(
                    f"\nPerdiste... El crupier sacó {crupierScore} y tú {playerScore}")
                if hasDividedCards:
                    print(
                        f"\nHas perdido una mano, te queda la otra mano.")
                    return removeHand(playerHand)

                print(
                    f"Has perdido ${amountToBet}")

                newBalance = playerMoney - amountToBet
                menu_casino.updateMoney(userId, newBalance)

                break

            elif (crupierScore < playerScore):
                print(
                    f"\n¡Ganaste! El crupier sacó {crupierScore} y tú {playerScore}")
                print(f"Has ganado ${amountToBet * 2}")

                newBalance = playerMoney + (amountToBet * 2)
                menu_casino.updateMoney(userId, newBalance)

                break

    stayPlayingOrReturn()


def getCardValues(cards):
    values = []
    specialValues = ["J", "Q", "K"]

    for i in range(len(cards)):
        value = cards[i][:2]
        value = value.replace(" ", "")

        if (value in specialValues):
            values.append(10)
            continue

        values.append(int(value))

    return values


def removeHand(playerHand):
    global hasDividedCards
    global playerCards

    hasDividedCards = False

    for i in range(len(playerCards)):
        if playerHand == playerCards[i]:
            continue

        playerCards = playerCards[i]
        break

    menu()


def stayPlayingOrReturn():
    global userId
    global userPin
    global userName

    print("\n¿Desea volver a jugar Blackjack?")
    print("1) Sí")
    print("2) No")

    while True:
        option = input(">>> ")
        if (option == "1" or option == "2"):
            break
        else:
            print("Opción inválida, reintente...")

    if option == "1":
        start(userId, userPin, userName)
    else:
        user_authentication.menuCasino(userId, userPin, userName)


def menu():
    printMenu()
    option = getMenuOption()
    handleMenuOption(option)


def printMenu():
    global playerMoney

    print(f"\n♦ Menú del Blackjack ♦ (Saldo actual: ${playerMoney})")
    print("1) Pedir Carta")
    print("2) Deseo parar")
    print("3) Consultar mis Cartas")
    print("4) Consultar carta del Crupier")


def getMenuOption():
    while True:
        option = input(">>> ")
        if isValidMenuOption(option):
            break
        print("Opción inválida, reintente...")

    return option


def isValidMenuOption(option):
    validOptions = ["1", "2", "3", "4"]

    isValidOption = option in validOptions
    return isValidOption


def handleMenuOption(option):
    if option == "1":
        requestNewCard()
    elif option == "2":
        stand()
    elif option == "3":
        printPlayerCards()
    elif option == "4":
        printCrupierCards()


def requestNewCard():
    global hasDividedCards
    global playerCards

    if hasDividedCards:
        playerHand = getHand()
        addNewCardToHand(playerHand)
        checkScore(playerHand)
    else:
        addNewCardToHand(playerCards)
        checkScore(playerCards)

    menu()


def getHand():
    global playerCards

    print("\n¿A cuál mano desea agregar una nueva carta?")
    print("1) Mano 1")
    print("2) Mano 2")
    option = getHandOption()

    return playerCards[int(option) - 1]


def getHandOption():
    while True:
        option = input(">>> ")

        if isValidHandOption(option):
            break

        print("Opción inválida, reintente...")

    return option


def isValidHandOption(option):
    return option == "1" or option == "2"


def addNewCardToHand(playerHand):
    newCard = getRandomCard("player")
    playerHand.append(newCard)

    print(f"\nHa obtenido un {newCard}")


def stand():
    global hasDividedCards
    global playerCards

    if hasDividedCards:
        checkBlackjack(playerCards[0])
    else:
        checkBlackjack(playerCards)


def printPlayerCards():
    global hasDividedCards

    print("\nMis cartas")
    if hasDividedCards:
        printTwoHands()
    else:
        printTheOnlyHand()


def printTheOnlyHand():
    global playerCards
    for i in range(len(playerCards)):
        print(playerCards[i])
    print(f"Sumatoria: {sum(getCardValues(playerCards))}")

    menu()


def printTwoHands():
    global playerCards
    for i in range(len(playerCards)):
        print(f"\nCartas de la mano {i + 1}:")
        for j in range(len(playerCards[i])):
            print(playerCards[i][j])
        print(f"Sumatoria: {sum(getCardValues(playerCards[i]))}")

    menu()


def printCrupierCards():
    global crupierCards

    print("\nCartas del Crupier")
    for i in range(len(crupierCards)):
        isFirstCard = i == 0
        if isFirstCard:
            print("La primer carta del crupier está oculta.")
            continue

        print(crupierCards[i])

    menu()
