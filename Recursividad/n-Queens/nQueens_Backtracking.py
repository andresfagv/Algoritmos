def place_queen(row, queens , n):
    if row == n:
        print(queens)
        return 1
    else:
        total_sol = 0
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row]
                place_queen(row+1, queens, n)




def n_queens(n):
    queens = ['']*n
    row = 0
    return place_queen(row, queens, n)