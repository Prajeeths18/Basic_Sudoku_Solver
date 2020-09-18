def print_board(boa):
    for row in boa:
        print(*row)


def find_empty(boa):
    for row_idx in range(9):
        for col_idx in range(9):
            if boa[row_idx][col_idx] == 0:
                return row_idx, col_idx
    return None


def valid(boa, row, col, num):
    for i in range(len(boa[row])):
        if col != i and num == boa[row][i]:
            return False

    for i in range(len(boa)):
        if row != i and num == boa[i][col]:
            return False

    start_row = row - row%3
    start_col = col - col%3

    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if boa[i][j] == num and (i,j) != (row,col):
                return False

    return True


def solve_board(boa):
    pos = find_empty(boa)
    if pos is None:
        return True

    row, col = pos

    for num in range(1,10):
        if valid(boa,row,col,num):
            boa[row][col] = num

            if solve_board(boa):
                return True

            boa[row][col] = 0

    return False


def am_i_right(boa):
    for row in boa:
        if len(set(row)) != 9:
            return False

    for col in range(9):
        set_col = set()
        for row in boa:
            set_col.add(row[col])
        if len(set_col) != 9:
            return False

    for start_row in range(0,7,3):
        for start_col in range(0,7,3):
            set_box = set()
            for row in range(start_row,start_row+3):
                set_box=set_box.union(set(boa[row][start_col:start_col+3]))
            if len(set_box) != 9:
                return False
    return True