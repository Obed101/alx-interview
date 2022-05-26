#!/usr/bin/python3
"""This program solves the N-QUEENS problem"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

arg = sys.argv[1]

try:
    int(arg)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (int(arg) >= 4):
    print("N must be at least 4")
    sys.exit(1)
arg = int(arg)


def solveNQueens(n):
    """Solution for n queens"""
    col = set()
    pos = set()
    neg = set()

    res = []

    board = [[] for n in range(n)]

    def backtrack(row):
        """function for recursion"""
        if row == n:
            copy = board.copy()
            res.append(copy)
            return

        for c in range(n):
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            board[row] = [row, c]
            backtrack(row + 1)

            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            board[row] = []
    backtrack(0)

    return res


if __name__ == "__main__":
    boards = solveNQueens(arg)
    for board in boards:
        print(board)
