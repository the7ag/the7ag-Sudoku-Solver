board = [[7, 0, 2, 0, 5, 0, 6, 0, 0], [0, 0, 0, 0, 0, 3, 0, 0, 0], [1, 0, 0, 0, 0, 9, 5, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 9, 0], [0, 4, 3, 0, 0, 0, 7, 5, 0], [0, 9, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 9, 7, 0, 0, 0, 0, 5], [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 7, 0, 4, 0, 2, 0, 3]]
Grid_Size = 9


def printBoard(b):
    for i in range(Grid_Size):
        if i % 3 == 0 and i != 0:
            print("---------")
        for j in range(Grid_Size):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            print(b[i][j], end="")
        print()


def CheckAll(x, y, n):
    global board
    for i in range(0, Grid_Size):
        if board[y][i] == n:
            return False
    for i in range(0, Grid_Size):
        if board[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        if board[y0 + i][x0 + i] == n:
            return False
    return True


def solve():
    global board
    for y in range(Grid_Size):
        for x in range(Grid_Size):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if CheckAll(x, y, n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    printBoard(board)
    input("More")


solve()
