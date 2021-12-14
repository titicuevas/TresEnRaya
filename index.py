tablero=(" " * 9) #Nuestras casillas creadas estan vacias
#Colocamos una ficha en el tablero
def coordenada(literal,inferior,superior):
    while True:
     Valor=input(literal)
     while(not Valor.isnumeric()):
         print("Solo se admiten numeros entre {0} y {1}".format(inferior,superior))
         valor=input(literal)
     coor=int(valor)
     if (coor>inferior and superior <=superior):
         return coor
     
    else:
        print("El valor indicado es incorrecto,introduzca un numero entre {0} y {1}".format(inferior,superior))
    
    
def colocarFicha(ficha):
    print("Dame la posicion de una ficha")
    while True:
        fila=coordenada("Fila: ")
        columna=coordenada("Columna: ")
        
        #Es un tablero 3x3
        casilla=fila*3+columna
        if(tablero[casilla]!=' '):
            #Casilla cubierta
            print("La casilla esta ocupada")
        else:
            tablero[casilla]=ficha
            return
        

jugador1=input("Introduzca el nombre del jugador 1: ")
jugador2=input("Introduzca el nombre del jugador 2: ")


#Inicio el juego

continuar=True
fichasEnTablero=0
while continuar:
    #Pedimos posicion fichas
    
    colocarFicha('X'if (fichasEnTablero&1)else 'O')
    fichasEnTablero+=1
    if(fichasEnTablero==9):
        continuar=False
    