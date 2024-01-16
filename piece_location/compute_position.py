import numpy as np

# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

class BoardComparator:
    def __init__(self, fen, turn):
        # this creates an empty 8x8 array for the chessboard
        self.fen = fen
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.turn = turn
        
        position_fen = fen.split(" ")[0].split("/")
        for row in range(len(position_fen)):
            for col in range(len(position_fen[row])):
                if position_fen[row][col].isnumeric():
                    pass
                else:
                    if position_fen[row][col].isupper():
                        self.board[row][col] = 1
                    else:
                        self.board[row][col] = 2
        
    def make_move(self, newboard):
        for row in range(8):
            for col in range(8):
                if newboard[row][col] != self.board[row][col]:
                    if newboard[row][col] == 
                        from_tile = (row, col)
                    else:
                        
                
    def get_fenstring():
        pass

if __name__ == "__main__":
    comparator = BoardComparator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    