def print_chessboard(chessboard):
    white_pieces = ["♖", "♘", "♗", "♔", "♕", "♗", "♘", "♖"]
    black_pieces = ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]
    white_pawn = "♙"
    black_pawn = "♟"
    empty_square_dark = "◼"
    empty_square_light = "◻"

    for i in range(8):
        for j in range(8):
            piece = chessboard[i][j]
            if piece == white_pawn:
                print(f" {white_pawn} ", end="")
            elif piece == black_pawn:
                print(f" {black_pawn} ", end="")
            elif piece in white_pieces:
                print(f" {piece} ", end="")
            elif piece in black_pieces:
                print(f" {piece} ", end="")
            else:
                square_type = empty_square_dark if (i + j) % 2 == 0 else empty_square_light
                print(f" {square_type} ", end="")

        print()  # Move to the next line after printing a row

def move_piece(chessboard, from_square, to_square, move_list):
    from_row, from_col = 8 - int(from_square[1]), ord(from_square[0]) - ord('a')
    to_row, to_col = 8 - int(to_square[1]), ord(to_square[0]) - ord('a')
    chessboard[to_row][to_col] = chessboard[from_row][from_col]
    chessboard[from_row][from_col] = ' '

    # Save the current state of the chessboard after the move
    move_list.append([chessboard[i][:] for i in range(8)])

if __name__ == "__main__":
    initial_chessboard = [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
    ]

    move_list = []  # List to store the chessboard state after each move

    print("Initial Chessboard:")
    print_chessboard(initial_chessboard)

    # Move a piece
    move_piece(initial_chessboard, "e2", "e4", move_list)

    print("\nAfter moving pawn from e2 to e4:")
    print_chessboard(initial_chessboard)

    # Example: Accessing the state after the first move
#    print("\nChessboard state after the first move:")
#    print_chessboard(move_list[0])
    
     # Move a piece
    move_piece(initial_chessboard, "d2", "d4", move_list)
    print("\nAfter moving pawn from d2 to d4:")
    print_chessboard(initial_chessboard)

         # Move a piece
    move_piece(initial_chessboard, "a1", "a4", move_list)
    print("\nAfter moving pawn from a1 to a4:")
    print_chessboard(initial_chessboard)