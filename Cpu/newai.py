import chess
import chess.engine
from received import *
from dotenv import load_dotenv, find_dotenv
from os import environ as env
import pickle
import os
import shutil



load_dotenv(find_dotenv())
LC0_BINARY = env.get("LC0_BINARY") # Path to the Lc0 binary
LC0_WEIGHTS= env.get("LC0_WEIGHTS") # Path to the Lc0 neural network weights file


# Initialize the Lc0 engine
lc0 = chess.engine.SimpleEngine.popen_uci(LC0_BINARY)

# Set the Lc0 neural network weights
lc0.configure({"WeightsFile": LC0_WEIGHTS})
board = chess.Board()

# this is the color of the AI
def reset_board(isWhite):
    global board
    board = chess.Board()
    cleanup()
    if isWhite:
        result = lc0.play(board, chess.engine.Limit(time=0.1))
        best_move = result.move
        # Print the move played
        print("Lc0 plays:", best_move)

        # Update the board
        board.push(best_move)

        received(board.fen())
        print("fen: " + board.fen())
        # Close the Lc0 engine lc0.quit()
        print(board)
        write_variable(2)
        return str(best_move)
    write_variable(1)


def chessmove(move):
    board.push_san(move)
    print(board)
    # Play a move with Lc0
    result = lc0.play(board, chess.engine.Limit(time=0.1))
    best_move = result.move
    # Print the move played
    print("Lc0 plays:", best_move)

    # Update the board
    board.push(best_move)

    # Close the Lc0 engine lc0.quit()
    print(board)
    received(board.fen())
    print("fenstring: " + board.fen())
    return str(best_move)

def ifover():
    if (board.is_checkmate() or board.is_stalemate() or board.outcome() or board.can_claim_draw() or board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or board.is_insufficient_material() or board.is_fivefold_repetition() or board.is_seventyfive_moves()):
        print("The game is over")
def cleanup():
    if os.path.exists('AIcolor.pkl'):
        os.remove('AIcolor.pkl')
    if os.path.exists('out'):
        shutil.rmtree('out')
    if os.path.exists('cropped.png'):
        os.remove('cropped.png')
    if os.path.exists('Detected_Lines.png'):
        os.remove('Detected_Lines.png')
    if os.path.exists('initial_array.pkl'):
        os.remove('initial_array.pkl')
 
    
    
def write_variable(value):
    filename = "AIcolor.pkl"
    with open(filename, "wb") as file:
        pickle.dump(value, file)   