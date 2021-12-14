import math

tablero = []  # Nuestras casillas creadas estan vacias
TABLERO_FILAS = 3
TABLERO_COLUMNAS = 3
# Inicializamos el tablero
for i in range(9):
    tablero.append(" ")


# Colocamos una ficha en el tablero
def coordenada(literal, inferior, superior):
    while True:
        valor = input(literal)
        while not valor.isnumeric():
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
        casilla = fila * TABLERO_FILAS + columna
        if (tablero[casilla] != " "):
            # Casilla cubierta
            print("La casilla esta ocupada")
        else:
            tablero[casilla] = ficha
            return casilla


def pintarTablero():
    pos = 0
    print("-" * 18)
    for fila in range(3):
        for columna in range(3):
            print("| ", tablero[pos], " ", end="")
            pos += 1
        print("|\n", ("-" * 18))


def numeroHermanos(casilla, ficha, v, h):
    f = math.floor(casilla / TABLERO_COLUMNAS)  # obtengo la fila
    c = casilla % TABLERO_COLUMNAS  # obtengo la columna
    fila_nueva = f + v
    if (fila_nueva < 0 or fila_nueva >= TABLERO_FILAS):

        return 0
    
    columna_nueva = c + h
    if (columna_nueva < 0 or columna_nueva >= TABLERO_COLUMNAS):
        return 0
    # No estamos en el limite y calculamos la posicoon

    pos = (fila_nueva * TABLERO_COLUMNAS + columna_nueva)
    if (tablero[pos] != ficha):
        return 0
    else:
        return 1 + numeroHermanos(pos, ficha, v, h)


# Comprobar en la casilla adecuada no tiene 2 fichas iguales en casillas contiguas
def hemosGanado(casilla, ficha):
    hermanos = numeroHermanos(casilla, ficha, -1, -1) + numeroHermanos(
        casilla, ficha, 1, 1
    )
    if (hermanos == 2):
        return True
    
    hermanos = numeroHermanos(casilla, ficha, 1, -1) + numeroHermanos(
        casilla, ficha, -1, 1
    )
    if (hermanos == 2):
        return True
    
        hermanos = numeroHermanos(casilla, ficha, -1, 0) + numeroHermanos(
            casilla, ficha, 1, 0
        )
    if (hermanos == 2):
        return True
    
    hermanos = (
        numeroHermanos(casilla, ficha, 0, -1) + numeroHermanos(casilla, ficha, 0, 1)
    )
    if (hermanos == 2):
        return True

jugadores=[]

jugadores.append(input("Introduzca el nombre del jugador 1: "))
jugadores.append (input("Introduzca el nombre del jugador 2: "))


# Inicio el juego

continuar = True
fichasEnTablero = 0
while continuar:

    # Pedimos posicion fichas
    pintarTablero()
    jugador=(fichasEnTablero&1)
    ficha='X'if jugador==1 else 'O'
    casilla = colocarFicha(ficha)
    if (hemosGanado(casilla, ficha)):
        continuar = False
        print(jugadores[jugador] ,"Has Ganado!!!!!!")
    fichasEnTablero += 1
    if fichasEnTablero == 9:
        continuar = False
pintarTablero()
