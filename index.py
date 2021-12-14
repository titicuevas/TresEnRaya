tablero = []  # Nuestras casillas creadas estan vacias

# Inicializamos el tablero
for i in range(9):
    tablero.append(" ")


# Colocamos una ficha en el tablero
def coordenada(literal, inferior, superior):
    while True:
        valor = input(literal)
        while (not valor.isnumeric()):
            print("Solo se admiten numeros entre {0} y {1}".format(inferior, superior))
            valor = input(literal)
        coor = int(valor)
        if coor >= inferior and coor <= superior:
            return coor

    else:
        print(
            "El valor indicado es incorrecto,introduzca un numero entre {0} y {1}".format(
                inferior, superior
            )
        )


def colocarFicha(ficha):
    print("Dame la posicion de una ficha")
    while True:
        fila = coordenada("Fila entre [1-3]: ", 1, 3) - 1
          # Restamos 1 para que sea de 0-2
        columna = coordenada("Columna entre [1-3]: ", 1, 3) - 1
          # Restamos 1 para que sea de 0-2

        # Es un tablero 3x3
        casilla = fila * 3 + columna
        if tablero[casilla] != " ":
            # Casilla cubierta
            print("La casilla esta ocupada")
        else:
            tablero[casilla] = ficha
            return


def pintarTablero():
    pos=0
    print("-" * 18)
    for fila in range(3):
        for columna in range(3):
            print("| ", tablero[pos], " ", end="")
            pos+= 1
        print("|\n", ("-" * 18))


jugador1 = input("Introduzca el nombre del jugador 1: ")
jugador2 = input("Introduzca el nombre del jugador 2: ")


# Inicio el juego

continuar = True
fichasEnTablero = 0
while continuar:

    # Pedimos posicion fichas
    pintarTablero()
    colocarFicha("X" if (fichasEnTablero & 1) else "O")

    fichasEnTablero += 1
    if fichasEnTablero == 9:
        continuar = False
