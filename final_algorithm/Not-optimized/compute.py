# curBoard is the current 2d array
# newBoard is the new board after the move has been played
# turn should be 1 if it was white to move and 2 if it was black to move
def findMove(curBoard, newBoard, turn):
    differences = []
    digitToLetters = list(map(chr, range(97, 123)))[0 : 8]
    move = ""
    
    for i in range(8):
        for j in range(8):
            if curBoard[i][j] != newBoard[i][j]:
                differences.append((i, j))
    if len(differences) > 2:
        pass
    if len(differences) == 2:
        if curBoard[differences[0][0]][differences[0][1]] == turn:
            move += (digitToLetters[differences[0][1]] + str(8 - differences[0][0]))
            move += (digitToLetters[differences[1][1]] + str(8 - differences[1][0]))
        else:
            move += (digitToLetters[differences[1][1]] + str(8 - differences[1][0]))
            move += (digitToLetters[differences[0][1]] + str(8 - differences[0][0]))
    print(differences)
    return move
            

print(changeBoard([
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ],
        [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ], 1))

# class ChessArrayComparator:
#     def __init__(self, initial_array):
#         self.previous_array = initial_array

#     def compare_and_update(self, new_array):
#         if self.is_equal(self.previous_array, new_array):
#             return "No move occurred"
#         else:
#             # Finds the differences in the previous board and the new
#             differences = self.find_differences(self.previous_array, new_array)
#             move_source_squares = [
#                 self.get_chess_movement(diff[0], diff[1], diff[2], self.previous_array, new_array)
#                 for diff in differences
#                 if self.get_chess_movement(diff[0], diff[1], diff[2], self.previous_array, new_array) is not None
#             ]

#             if not move_source_squares:
#                 return "No valid move detected"

#             # Sort the source squares based on the source squares themselves and the array index (reversed)
#             move_source_squares.sort(key=lambda x: (x.split()[-1], x), reverse=True)

#             return "\n".join(move_source_squares)

#     def is_equal(self, array1, array2):
#         return all(row1 == row2 for row1, row2 in zip(array1, array2))

#     # finds the difference between two 2d arrays.
#     def find_differences(self, array1, array2):
#         differences = []
#         for i, (row1, row2) in enumerate(zip(array1, array2)):
#             for j, (elem1, elem2) in enumerate(zip(row1, row2)):
#                 if elem1 != elem2:
#                     differences.append(((i, j), elem1, elem2))
#         return differences

#     def get_chess_movement(self, position, old_value, new_value, array1, array2):
#         row, col = position
#         file_char = chr(ord('a') + col)
#         rank = 8 - row
#         source_square = f"{file_char}{rank}"

#         if old_value == 0:
#             return f"{source_square} from array 0"
#         elif new_value == 0:
#             return f"{source_square} from array 1"
#         else:
#             return None

