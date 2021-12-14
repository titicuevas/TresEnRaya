jugador1=input("Introduzca el nombre del jugador 1: ")
jugador2=input("Introduzca el nombre del jugador 2: ")


#Inicio el juego
continuar=True
fichasEnTablero=0
while continuar:
    # Pedimos posicion fichas
    input("Dame la posicion de una ficha")
    fila=input("Fila: ")
    columna=input("Columna: ")
    fichasEnTablero+=1
    if(fichasEnTablero==9):
        continuar=False
    