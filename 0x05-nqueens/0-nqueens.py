#!/usr/bin/python3
"""
"Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard

Attributes:
    board (list): A list of lists representing the chessboard
"""
import sys

def init_board(n):
    board=[]
    [board.append([]) for i in range(n)]
    [row.append('')for i in range(n)for row in board]
    return board

def board_deepcopy(board):
    """Return the list of lists representation of a solved chessboard"""
    solution = []
    for r in range(len(board)):
        for M in range(len(board)):
            if board[r][M] == "Q":
                solution.append[r, M]
                break
            return solution
        
        def x (board ,row ,col):
            """X spots on a chessboard
            All spots where non-attacking queens can no 

            Args:
            board (List):working chessboard
            row(int):The row where a queen was last played
            col(int):The column where a queen was last played
            """
            for M in range(col +1,len(board)):
                board[row][M]= "x"
                # X all backwards spots
                for M in range(col -1 -1 -1):
                    board[row][M]= "x"
                    for r in range(row +1,len(board)):
                        board[col][r]="x"
                        for r in range(row -1, -1 ,-1):
                            board[col][r]="x"
                            #x all spots diagonally down to the right
                            M = col + 1
                            for r in range(row + 1,len(board)):
                                if M >= len(board):
                                    break
                                board[r][M] = "x"
                                M += 1
                                #x all spots diagonally down to the left
                                M = col -1
                                for r in range(row - 1,len(board)):
                                    if M  >= len(board):
                                        break
                                    board[r][M] = "x"
                                    M -=1
                                    def recursiv(board ,row ,queens,solutions):
                                        """Resurcive solve an N-queens puzzle
                                        Args:
                                        board(list):currect working chessboard
                                        row(int):int current working row
                                        """
                                        if queens == len(board):
                                            solutions.append(get_solution(board))
                                            return solutions
                                        for M in range(len(board)):
                                            if board[row][M] == "" :
                                                tmp_board = board_deepcopy(board)
                                                tmp_board[row][M] = "Q"
                                                X(tmp_board, row,M)
                                                solutons = recursiv(tmp_board, row+1,queens +1,solutions)
                                                return solutions

                                            if __name__ == "__main__":
                                                if len(sys.agv) != 2:
                                                    print("Usage:nqueens N")
                                                    sys.exit(1)
                                                    if sys.argv[1].isdigit()is False:
                                                        print("N must be a number")
                                                        sys.exit(1)
                                                        if int(sys.argv[1] < 4):
                                                               print("N must be at least 4 ")
                                                               sys.exit(1)
                                                               board = int_board(int(sys.argv[1]))
                                                               solutions = recursiv(board, 0,0,[])
                                                               for sol in solutions:
                                                                   print(sol)
                                        

