class ChessArrayComparator:
    def __init__(self, initial_array):
        self.previous_array = initial_array

    def compare_and_update(self, new_array):
        if self.is_equal(self.previous_array, new_array):
            print("Arrays are equal.")
        else:
            print("Arrays are not equal. Updating previous array.")
            differences = self.find_differences(self.previous_array, new_array)
            print("Differences:")
            for diff in differences:
                move_str = self.get_chess_movement(diff[0], diff[1], diff[2])
                if move_str is not None:
                    print(f"Move: {move_str}")
            self.previous_array = new_array

    def is_equal(self, array1, array2):
        # Compare two arrays element-wise
        return all(row1 == row2 for row1, row2 in zip(array1, array2))

    def find_differences(self, array1, array2):
        differences = []
        for i, (row1, row2) in enumerate(zip(array1, array2)):
            for j, (elem1, elem2) in enumerate(zip(row1, row2)):
                if elem1 != elem2:
                    differences.append(((i, j), elem1, elem2))
        return differences

    def get_chess_movement(self, position, old_value, new_value):
        # Convert array indices to chess coordinates
        row, col = position
        file_char = chr(ord('a') + col)
        rank = 8 - row
        source_square = f"{file_char}{rank}"

        # Determine destination square based on the change in values
        if old_value == 0:
            dest_square = f"{file_char}{8 - row - 1}"  # Use new row index
        elif new_value == 0:
            dest_square = f"{file_char}{8 - row}"  # Use new row index
        else:
            dest_square = f"{file_char}{8 - int(new_value)}"

        # Only return the movement if the source and destination squares are different
        if source_square != dest_square:
            return f"{dest_square} to {source_square}"
        else:
            return None

if __name__ == "__main__":
    # Initial chessboard array
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

    # Create an instance of ChessArrayComparator
    comparator = ChessArrayComparator(initial_array)

    # Example comparisons
    new_array1 = [
        [2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

    comparator.compare_and_update(new_array1)

    new_array2 = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

    comparator.compare_and_update(new_array2)