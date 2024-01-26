class ArrayComparator:
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
                print(f"At position {diff[0]}, value changed from {diff[1]} to {diff[2]}.")
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

if __name__ == "__main__":
    # Initial array
    newboard = [
        [2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Create an instance of ArrayComparator
    comparator = ArrayComparator(newboard)

    # Example comparisons
    new_array1 = [
        [2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]

    comparator.compare_and_update(new_array1)

