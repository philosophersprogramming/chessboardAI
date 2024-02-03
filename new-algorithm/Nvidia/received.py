import pickle
def received(move):
    try:
        with open('initial_array.pkl', 'rb') as initial_file:
            initial_array = pickle.load(initial_file)
    except FileNotFoundError:
        # If the file is not found, use the default initial array
        initial_array = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def make_move(chessboard, move):
        from_row, from_col, to_row, to_col = 8 - int(move[1]) , ord(move[0]) - ord('a'), 8 - int(move[3]) , ord(move[2]) - ord('a')

        if 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8:
            piece_value = chessboard[from_row][from_col]
            chessboard[to_row][to_col] = piece_value
            chessboard[from_row][from_col] = 0
        else:
            print("Invalid move. Out of bounds.")

    # Example usage:


    make_move(initial_array, move)  # Corrected move to "a7a5"

    print("\nAfter move:")
    for row in initial_array:
        print(row)

    with open('initial_array.pkl', 'wb') as initial_file:
        pickle.dump(initial_array, initial_file)

