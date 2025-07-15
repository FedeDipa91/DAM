from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]]
linea_horizontal = '+-------+-------+-------+'
linea_vacia = '|       |       |       |'

def display_board(board):

    '''La función acepta un parámetro el cual contiene el estado actual del tablero
     y lo muestra en la consola.'''
    
    for i in range(3):
        print(linea_horizontal)
        print(linea_vacia)
        print(f'|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |' )
        print(linea_vacia)
    print(linea_horizontal)
    

def make_list_of_free_fields(board):
    '''La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.'''
    free_fields = []
    for i in range (3):
        for j in range(3):
            if board[i][j] in ('X','O'):
                continue
            else:
                free_fields.append((i,j))
    return(free_fields)



def enter_move(board):
    #¿Cómo conviertes el número de cuadro (1-9) a coordenadas [fila][columna]?
    #¿Qué validaciones necesitas?

    '''La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario.'''
    while True:
        user_move = int(input('Ingresa tu movimiento: '))
        num_ajustado = user_move - 1
        coordenadas = (num_ajustado // 3, num_ajustado % 3)

        if user_move in range(1,10) and coordenadas in make_list_of_free_fields(board):
            break
    
    fila, columna = coordenadas
    board[fila][columna] = 'O'

def draw_move(board):
    '''La función dibuja el movimiento de la máquina y actualiza el tablero.'''
    free_cels = make_list_of_free_fields(board)
    index = randrange(len(free_cels))
    fila,columna = free_cels[index]
    board[fila][columna] = 'X'


def victory_for(board, sign):

    """
    La función analiza el estatus del tablero para verificar si 
    el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    """
    
    # Verificar filas horizontales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
    
    # Verificar columnas verticales
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == sign:
            return True
    
    # Verificar diagonal principal (esquina superior izquierda a inferior derecha)
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    
    # Verificar diagonal secundaria (esquina superior derecha a inferior izquierda)
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    
    # Si no hay victoria
    return False



# =================== JUEGO PRINCIPAL ===================

print("¡Bienvenido al Tic-Tac-Toe!")
print("Tú juegas con 'O', la máquina con 'X'")
print("La máquina comienza:")

# La máquina hace el primer movimiento (centro)
board[1][1] = 'X'
display_board(board)

# Bucle principal del juego
while True:
    # Turno del usuario
    enter_move(board)
    display_board(board)
    
    # Verificar si el usuario ganó
    if victory_for(board, 'O'):
        print("¡Felicidades! ¡Has ganado!")
        break
    
    # Verificar empate
    if len(make_list_of_free_fields(board)) == 0:
        print("¡Es un empate!")
        break
    
    # Turno de la máquina
    print("Turno de la máquina...")
    draw_move(board)
    display_board(board)
    
    # Verificar si la máquina ganó
    if victory_for(board, 'X'):
        print("La máquina ha ganado. ¡Mejor suerte la próxima vez!")
        break
    
    # Verificar empate después del movimiento de la máquina
    if len(make_list_of_free_fields(board)) == 0:
        print("¡Es un empate!")
        break