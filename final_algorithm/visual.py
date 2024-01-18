def print_chessboard():
    white_pieces = ["♖", "♘", "♗", "♔", "♕", "♗", "♘", "♖"]
    black_pieces = ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]
    white_pawn = "♙"
    black_pawn = "♟"
    empty_square_dark = "◼"
    empty_square_light = "◻"

    for i in range(8):
        for j in range(8):
            if i == 1:
                print(f" {white_pawn} ", end="")
            elif i == 6:
                print(f" {black_pawn} ", end="")
            elif i == 0:
                print(f" {white_pieces[j]} ", end="")
            elif i == 7:
                print(f" {black_pieces[j]} ", end="")
            else:
                square_type = empty_square_dark if (i + j) % 2 == 0 else empty_square_light
                print(f" {square_type} ", end="")

        print()  # Move to the next line after printing a row

if __name__ == "__main__":
    print_chessboard()
