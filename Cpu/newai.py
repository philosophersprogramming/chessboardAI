import chess
import chess.engine
from received import *

# Path to the Lc0 binary
LC0_BINARY = "/opt/homebrew/bin/lc0"

# Path to the Lc0 neural network weights file
LC0_WEIGHTS = "/Users/akash/Source/maia-chess/maia_weights/maia-1100.pb.gz"

# Initialize the Lc0 engine
lc0 = chess.engine.SimpleEngine.popen_uci(LC0_BINARY)

# Set the Lc0 neural network weights
lc0.configure({"WeightsFile": LC0_WEIGHTS})
# board = chess.Board()

# this is the color of the AI
def reset_board(isWhite):
    global board
    board = chess.Board()
    if isWhite:
        result = lc0.play(board, chess.engine.Limit(time=0.1))
        best_move = result.move
        # Print the move played
        print("Lc0 plays:", best_move)

        # Update the board
        board.push(best_move)

        # Close the Lc0 engine lc0.quit()
        print(board)
        received(str(best_move))


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
    received(str(best_move))
    return str(best_move)
