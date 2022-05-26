#!/usr/bin/python3
"""This program solves the N-QUEENS problem"""
import sys
from click import echo

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


def setup_n_queens(n):
    """This function sets N Queens table"""
    column = set()
    forward = set()
    backward_ = set()

    table = []

    board = [[] for n in range(n)]

    def backtrack(row):
        """Semi callback for Backtrack algorithm"""
        if row == n:
            copy = board.copy()
            table.append(copy)
            return

        for col in range(n):
            if col in column or (row + col) in forward or (row - col) in backward_:
                continue

            column.add(col)
            forward.add(row + col)
            backward_.add(row - col)

            board[row] = [row, col]
            backtrack(row + 1)

            column.remove(col)
            forward.remove(row + col)
            backward_.remove(row - col)
            board[row] = []
    backtrack(0)

    return table


if __name__ == "__main__":
    boards = setup_n_queens(arg)
    for board in boards:
        print(board)
