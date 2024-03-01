import pickle

def received(move):
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

    def make_move(chessboard, move):
        # Determine the color of the piece
        from_row, from_col, to_row, to_col = 8 - int(move[1]), ord(move[0]) - ord('a'), 8 - int(move[3]), ord(move[2]) - ord('a')

    # Determine the color of the piece
        piece_value = chessboard[from_row][from_col]

        if piece_value == 0:
            print("No piece found at the starting position.")
            return
        elif piece_value == 1:
            print("White piece moved.")
        elif piece_value == 2:
            print("Black piece moved.")

        # Check if it's a castling move
        if move.lower() == "o-o":
            if piece_value == 1:  # White king-side castling
                from_row, from_col, to_row, to_col = 7, 4, 7, 6
            elif piece_value == 2:  # Black king-side castling
                from_row, from_col, to_row, to_col = 0, 4, 0, 6
        elif move.lower() == "o-o-o":
            if piece_value == 1:  # White queen-side castling
                from_row, from_col, to_row, to_col = 7, 4, 7, 2
            elif piece_value == 2:  # Black queen-side castling
                from_row, from_col, to_row, to_col = 0, 4, 0, 2
        else:
            from_row, from_col, to_row, to_col = 8 - int(move[1]), ord(move[0]) - ord('a'), 8 - int(move[3]), ord(move[2]) - ord('a')

        if 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8:
            # Handle castling moves
            if move.lower() == "o-o" and chessboard[from_row][from_col] == piece_value:
                chessboard[to_row][to_col] = piece_value
                chessboard[from_row][from_col] = 0
                if piece_value == 1:  # White king-side castling
                    chessboard[7][7] = 0
                    chessboard[7][5] = piece_value
                elif piece_value == 2:  # Black king-side castling
                    chessboard[0][7] = 0
                    chessboard[0][5] = piece_value
            elif move.lower() == "o-o-o" and chessboard[from_row][from_col] == piece_value:
                chessboard[to_row][to_col] = piece_value
                chessboard[from_row][from_col] = 0
                if piece_value == 1:  # White queen-side castling
                    chessboard[7][0] = 0
                    chessboard[7][3] = piece_value
                elif piece_value == 2:  # Black queen-side castling
                    chessboard[0][0] = 0
                    chessboard[0][3] = piece_value
            else:
                chessboard[to_row][to_col] = piece_value
                chessboard[from_row][from_col] = 0
        else:
            print("Invalid move. Out of bounds.")

    make_move(initial_array, move)

    print("\nAfter move:")
    for row in initial_array:
        print(row)

    with open('initial_array.pkl', 'wb') as initial_file:
        pickle.dump(initial_array, initial_file)


# received("e2e4")