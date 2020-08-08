'''
    Using a backtracking algorithm to solve a given sudoku puzzle.
'''

board = [[0, 0, 0, 8, 0, 0, 0, 0, 9],
         [0, 1, 9, 0, 0, 5, 8, 3, 0],
         [0, 4, 3, 0, 1, 0, 0, 0, 7],
         [4, 0, 0, 1, 5, 0, 0, 0, 3],
         [0, 0, 2, 7, 0, 4, 0, 1, 0],
         [0, 8, 0, 0, 9, 0, 6, 0, 0],
         [0, 7, 0, 0, 0, 6, 3, 0, 0],
         [0, 3, 0, 0, 7, 0, 0, 8, 0],
         [9, 0, 4, 5, 0, 0, 0, 0, 1]]


def print_board(boa):
    for index, row in enumerate(boa):
        for idx, col in enumerate(row):
            print(col, end=" ")
        print("")


def valid(bo, num, row, col):
    # Check row
    for idx in range(len(bo[row])):
        if idx != col and bo[row][idx] == num:
            return False

    # Check col
    for idx in range(len(bo)):
        if idx != row and bo[idx][col] == num:
            return False

    start_row = row - (row % 3)
    start_col = col - (col % 3)

    # Check the 3 x 3 box
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if i == row and j == col:
                continue
            if bo[i][j] == num:
                return False

    return True


# print(valid(board, 2, 0, 0))

def find_empty(bo):
    for row_index in range(9):
        for col_index in range(9):
            if bo[row_index][col_index] == 0:
                return (row_index, col_index)

    return None


def solve_board(bo):
    find = find_empty(bo)

    if not find:
        return True

    row, col = find

    for i in range(1, 10):
        if valid(bo, i, row, col):
            bo[row][col] = i

            if solve_board(bo):
                return True

            bo[row][col] = 0

    return False


def is_valid(bo):
    for row in bo:
        s = set(row)
        if len(s) != 9:
            return False

    for i in range(len(bo[0])):
        s = set()
        for col in range(9):
            s.add(bo[i][col])
        if len(s) != 9:
            return False

    for st_row in range(0, 7, 3):
        for st_col in range(0, 7, 3):
            s = set()
            # print(st_row, " ", st_col)
            for row in range(st_row, st_row + 3):
                for col in range(st_col, st_col + 3):
                    s.add(bo[row][col])

            if len(s) != 9:
                return False

    return True


solve_board(board)
print_board(board)

print(is_valid(board))
