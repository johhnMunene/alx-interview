#!/usr/bin/env python3
""
import sys

def init_board(n):
    """
    Initializes an empty chessboard of size n x n.
    """
    board = [['' for _ in range(n)] for _ in range(n)]
    return board

def get_solution(board):
    """
    Returns the solution from the given board configuration.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append((r, c))
                break
    return solution

def mark_attacking_positions(board, row, col):
    """
    Marks the attacking positions of a queen placed at (row, col).
    """
    n = len(board)
    # Mark horizontal and vertical positions
    for i in range(n):
        board[row][i] = "x"
        board[i][col] = "x"
    # Mark diagonal positions
    for i, j in zip(range(row+1, n), range(col+1, n)):
        if i < n and j < n:
            board[i][j] = "x"
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if i >= 0 and j < n:
            board[i][j] = "x"
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if i < n and j >= 0:
            board[i][j] = "x"
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if i >= 0 and j >= 0:
            board[i][j] = "x"

def solve_nqueens(board, row, queens, solutions):
    """
    Recursive function to solve the N-queens puzzle.
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions
    
    for col in range(n):
        if board[row][col] == "":
            tmp_board = [row[:] for row in board]  # Create a copy of the board
            tmp_board[row][col] = "Q"  # Place a queen at (row, col)
            mark_attacking_positions(tmp_board, row, col)
            solutions = solve_nqueens(tmp_board, row+1, queens+1, solutions)
    
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = init_board(n)
    solutions = solve_nqueens(board, 0, 0, [])
    for sol in solutions:
        print(sol)
        
