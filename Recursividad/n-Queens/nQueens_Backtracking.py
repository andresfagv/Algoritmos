from traceback import print_exc


def is_valid(row ,col, queens):
    for r in range(row):
        if col == queens[r]: return False
        elif abs(col - queens[r]) == abs(row - r): return False
    return True


def place_queen(row, queens , n):
    if row == n:
        print(queens)
        print_sol(queens)
        return 1
    else:
        total_sol = 0
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                total_sol += place_queen(row+1, queens, n)
        return  total_sol

def print_sol(queens):
    col = len(queens)
    for i in range(col):
        print ('0'*queens[i] + 'Q' + '0'*(col - queens[i] - 1))

def n_queens(n):
    queens = ['']*n
    row = 0
    return place_queen(row, queens, n)

aux = n_queens(4)
print(aux)