import chess
import chess.engine
from received import *

# testing
# chess.STARTING_BOARD_FEN = ""
board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(r"/opt/homebrew/bin/stockfish")


def setPlayerTurn(isWhite, depth):
    if not isWhite:
        result = engine.play(board, chess.engine.Limit(depth=depth))  # Set a time limit for the engine's move
        best_move = result.move
    
        # Apply the engine's move to the board
        board.push(best_move)


def reset_board():
    global board
    board = chess.Board()

def chessmove(move, depth):
    board.push_san(move)
    print(board)
    # Get the best move from the engine
    result = engine.play(board, chess.engine.Limit(depth=depth))  # Set a time limit for the engine's move
    best_move = result.move
    
    # Apply the engine's move to the board
    board.push(best_move)
    print("Engine's Move:", best_move)
    print(board)
    received(str(best_move))
    return str(best_move)
