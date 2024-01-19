import numpy as np

# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

class BoardComparator:
    def __init__(self, fen, turn):
        # this creates an empty 8x8 array for the chessboard
        self.fen = fen
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        # 0 - empty square
        # 1 - white piece
        # 2 - black piece
        self.turn = turn
        
        position_fen = fen.split(" ")[0].split("/")
        for row in range(8):
            col = 0
            for piece in position_fen[row]:
                if piece.isnumeric():
                    for i in range(int(piece)):
                        self.board[row][col + i] = ''
                    col += int(piece)
                else:
                    self.board[row][col] = piece
                    col += 1
                
    def make_move(self, newboard):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == "":
                    convert_tile = 0
                elif self.board[row][col].isupper():
                    convert_tile = 1
                else:
                    convert_tile = 2
                    
                if newboard[row][col] != convert_tile:
                    if newboard[row][col] == self.turn:
                        to_tile = (row, col)
                    else:
                        from_tile = (row, col)
        self.board[to_tile[0]][to_tile[1]] = self.board[from_tile[0]][from_tile[1]]
        self.board[from_tile[0]][from_tile[1]] = ""
        print(self.board)
                    
    def get_fenstring(self):
        fen = ""
        for row in self.board:
            empty_counter = 0
            for piece in row:
                if piece == '':
                    empty_counter += 1
                else:
                    if empty_counter != 0:
                        fen += str(empty_counter)
                        empty_counter = 0
                    fen += piece
            if empty_counter != 0:
                fen += str(empty_counter)
            fen += "/"
        return fen

if __name__ == "__main__":
    comparator = BoardComparator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 1)
    print(comparator.get_fenstring())
    newboard = [
        [2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
    comparator.make_move(newboard)