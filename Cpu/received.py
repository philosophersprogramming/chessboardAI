import pickle

def received(fen):
    try:
        with open('initial_array.pkl', 'rb') as initial_file:
            initial_array = pickle.load(initial_file)
    except FileNotFoundError:
        # If the file is not found, use the default initial array
        initial_array = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

    # def make_move(chessboard, move):
    #     # Determine the color of the piece
    #     from_row, from_col, to_row, to_col = 8 - int(move[1]), ord(move[0]) - ord('a'), 8 - int(move[3]), ord(move[2]) - ord('a')

    # # Determine the color of the piece
    #     piece_value = chessboard[from_row][from_col]

    #     if piece_value == 0:
    #         print("No piece found at the starting position.")
    #         return
    #     elif piece_value == 1:
    #         print("White piece moved.")
    #     elif piece_value == 2:
    #         print("Black piece moved.")

    #     # Check if it's a castling move
    #     if move.lower() == "o-o":
    #         if piece_value == 1:  # White king-side castling
    #             from_row, from_col, to_row, to_col = 7, 4, 7, 6
    #         elif piece_value == 2:  # Black king-side castling
    #             from_row, from_col, to_row, to_col = 0, 4, 0, 6
    #     elif move.lower() == "o-o-o":
    #         if piece_value == 1:  # White queen-side castling
    #             from_row, from_col, to_row, to_col = 7, 4, 7, 2
    #         elif piece_value == 2:  # Black queen-side castling
    #             from_row, from_col, to_row, to_col = 0, 4, 0, 2
    #     else:
    #         from_row, from_col, to_row, to_col = 8 - int(move[1]), ord(move[0]) - ord('a'), 8 - int(move[3]), ord(move[2]) - ord('a')

    #     if 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8:
    #         # Handle castling moves
    #         if move.lower() == "o-o" and chessboard[from_row][from_col] == piece_value:
    #             chessboard[to_row][to_col] = piece_value
    #             chessboard[from_row][from_col] = 0
    #             if piece_value == 1:  # White king-side castling
    #                 chessboard[7][7] = 0
    #                 chessboard[7][5] = piece_value
    #             elif piece_value == 2:  # Black king-side castling
    #                 chessboard[0][7] = 0
    #                 chessboard[0][5] = piece_value
    #         elif move.lower() == "o-o-o" and chessboard[from_row][from_col] == piece_value:
    #             chessboard[to_row][to_col] = piece_value
    #             chessboard[from_row][from_col] = 0
    #             if piece_value == 1:  # White queen-side castling
    #                 chessboard[7][0] = 0
    #                 chessboard[7][3] = piece_value
    #             elif piece_value == 2:  # Black queen-side castling
    #                 chessboard[0][0] = 0
    #                 chessboard[0][3] = piece_value
    #         else:
    #             chessboard[to_row][to_col] = piece_value
    #             chessboard[from_row][from_col] = 0
    #     else:
    #         print("Invalid move. Out of bounds.")

    board = [[0 for _ in range(8)] for _ in range(8)]

    position_fen = fen.split(" ")[0].split("/")

    for row in range(len(position_fen)):
        offset = 0
        for col in range(len(position_fen[row])):
            if position_fen[row][col].isnumeric():
                offset += int(position_fen[row][col]) - 1
                print("offset")
                print(int(position_fen[row][col]))
            else:
                if(offset > 0):
                    print("hallo")
                    print(col + offset)
                if position_fen[row][col].isupper():
                    board[row][col + offset] = 1
                else:
                    board[row][col + offset] = 2

    print(board)

    print("\nAfter move:")
    for row in board:
         print(row)

    with open('initial_array.pkl', 'wb') as initial_file:
        pickle.dump(board, initial_file)


received("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1")

#chat gpt stuff below that Akash was trying out! ( it works when your not loading the board from the pickle file )
# def received(fen):   
#     try:
#         with open('initial_array.pkl', 'rb') as initial_file:
#             board = pickle.load(initial_file)
#     except FileNotFoundError:
#         # If the file is not found, use the default initial array
#         board = [[0 for _ in range(8)] for _ in range(8)]

#     position_fen = fen.split(" ")[0].split("/")

#     for row in range(len(position_fen)):
#         col = 0
#         for char in position_fen[row]:
#             if char.isdigit():
#                 col += int(char)
#             else:
#                 if char.isupper():
#                     board[row][col] = 1
#                 else:
#                     board[row][col] = 2
#                 col += 1

#     print("After Move")
#     for row in board:
#         print(row)

#     with open('initial_array.pkl', 'wb') as initial_file:
#         pickle.dump(board, initial_file)

# received("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1")