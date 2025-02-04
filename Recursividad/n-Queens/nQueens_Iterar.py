def n_queens(num):
    return [['0'] * num for _ in range(num)]

def print_table(table):
    for fila in table:
        print(' '.join(fila))
    print()

def place_queen(x, y, table, num):
    if table[x][y] == '0':
        table[x][y] = 'Q'
        no_places(x, y, num, table)
        return True
    return False

def no_places(x, y, num, table):
    # Marcar la fila y la columna
    for i in range(num):
        if table[x][i] != 'Q':  # Evitar sobrescribir la reina
            table[x][i] = '1'
        if table[i][y] != 'Q':  # Evitar sobrescribir la reina
            table[i][y] = '1'

    # Marcar diagonales
    for i in range(num):
        # Diagonal ↘ (abajo-derecha)
        if x + i < num and y + i < num and table[x + i][y + i] != 'Q':
            table[x + i][y + i] = '1'

        # Diagonal ↖ (arriba-izquierda)
        if x - i >= 0 and y - i >= 0 and table[x - i][y - i] != 'Q':
            table[x - i][y - i] = '1'

        # Diagonal ↙ (abajo-izquierda)
        if x + i < num and y - i >= 0 and table[x + i][y - i] != 'Q':
            table[x + i][y - i] = '1'

        # Diagonal ↗ (arriba-derecha)
        if x - i >= 0 and y + i < num and table[x - i][y + i] != 'Q':
            table[x - i][y + i] = '1'


def print_solutions(solutions, num):
    for index, solution in enumerate(solutions):
        print(f"Solución {index + 1}:")
        # Crear un tablero vacío
        table = [['0'] * num for _ in range(num)]

        # Colocar las reinas ('Q') en sus respectivas posiciones
        for x, y in solution:
            table[x][y] = 'Q'

        # Imprimir el tablero
        for fila in table:
            print(' '.join(fila))
        print()  # Espacio entre soluciones



# Tamaño del tablero
num = 4
soluciones_finales=[]

for _ in range(num):
    cont = 0
    table = n_queens(num)
    solucion_actual = []
    aux = place_queen(0, _, table, num)
    if aux:
        cont += 1
        solucion_actual.append((0, _))
    for i in range(num):
        for j in range(num):
            aux = place_queen(i, j, table, num)
            if aux:
                cont += 1
                solucion_actual.append((i,j))
    if cont == num:
        soluciones_finales.append(solucion_actual)


print_solutions(soluciones_finales, num)
