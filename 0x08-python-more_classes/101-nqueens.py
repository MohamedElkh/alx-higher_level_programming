#!/usr/bin/python3
"""Solves of the N-queens puzzle.

determines all possible solutions to placing N
N is non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to  4.

Attributes:
    board : A list of lists representing the chessboard.
    solutions : A list of lists containing solutions.

Solution are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively
"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized with 0's."""

    boards = []
    [boards.append([]) for x in range(n)]
    [r.append(' ') for i in range(n) for r in boards]

    return (boards)


def board_deepcopy(boards):
    """Return copy of a chessboard."""
    if isinstance(boards, list):
        return list(map(board_deepcopy, boards))

    return (boards)


def get_solution(boards):
    """Return the list of lists rep of a solved chessboard."""

    solutions = []

    for x in range(len(boards)):
        for i in range(len(boards)):

            if boards[x][i] == "Q":
                solutions.append([x, i])
                break

    return (solutions)


def xout(boards, rr, cl):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        boards : the current working chessboard.
        rr : the row where a queen was last played.
        cl : the column where a queen was last played.
    """

    # X out all forward spots
    for x in range(cl + 1, len(boards)):
        boards[rr][x] = "x"

    # X out all backwards spots
    for x in range(cl - 1, -1, -1):
        boards[rr][x] = "x"

    # X out all spots below
    for i in range(rr + 1, len(boards)):
        boards[i][cl] = "x"

    # X out all spots above
    for i in range(rr - 1, -1, -1):
        boards[i][cl] = "x"

    # X out all spots diagonally down to the right
    x = cl + 1

    for i in range(rr + 1, len(boards)):
        if x >= len(boards):
            break

        boards[i][x] = "x"
        x += 1

    # X out all spots diagonally up to the left
    x = cl - 1

    for i in range(rr - 1, -1, -1):
        if x < 0:
            break

        boards[i][x]
        x -= 1

    # X out all spots diagonally up to the right
    x = cl + 1
    for i in range(rr - 1, -1, -1):
        if x >= len(boards):
            break

        boards[i][x] = "x"
        x += 1

    # X out all spots diagonally down to the left
    x = cl - 1
    for i in range(rr + 1, len(boards)):
        if x < 0:
            break

        boards[i][x] = "x"
        x -= 1


def recursive_solve(boards, rr, queen, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        boards : current working chessboard.
        rr : current working row.
        queen : current number of placed queens.
        solutions: list of lists of solutions.
    """

    if queen == len(boards):
        solutions.append(get_solution(boards))

        return (solutions)

    for x in range(len(boards)):
        if boards[rr][x] == " ":

            tmp_b = board_deepcopy(boards)
            tmp_b[rr][x] = "Q"

            xout(tmp_b, rr, x)
            solutions = recursive_solve(tmp_b, rr + 1,
                                        queen + 1, solutions)

    return (solutions)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    boards = init_board(int(sys.argv[1]))
    solutions = recursive_solve(boards, 0, 0, [])
    for sl in solutions:
        print(sl)
