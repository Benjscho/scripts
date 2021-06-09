import timeit

def backtrackSolveNQueens(n: int):
    def isValid(board, row: int, col: int) -> bool:
        for i in range(col):
            if board[row][i] == 1:
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i, j = i-1, j-1
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i, j = i+1, j-1
        return True

    def recoverSol(board):
        res = []
        for row in board:
            s = ""
            for col in row:
                if col == 1:
                    s += "Q"
                elif col == 0:
                    s += "."
            res.append(s)
        return res

    solutions = []

    def solve(board, col: int) -> bool:
        if (col >= n):
            solutions.append(recoverSol(board))
            return False
        for i in range(n):
            if isValid(board, i, col):
                board[i][col] = 1
                solve(board, col+1)

                board[i][col] = 0
        return False


    grid = [[0]*n for _ in range(n)]
    solve(grid, 0)

    return solutions


#print(backtrackSolveNQueens(16))
def wrapper():
    return backtrackSolveNQueens(10)
print(len(wrapper()))
print(timeit.timeit(wrapper, number=1))


