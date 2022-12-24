"""
The input to your function will be a tuple of tuples. For example:

((5, 6, 7, 8),
 (3, 9, 2, 5),
 (2, 1, 9, 2))

Your function should return the index of the column with the highest sum.

Examples:

matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
top_column(matrix_1) => 2
Explanation: Column 2 has a sum of 18, higher than any other column.

matrix_2 = ((1, 2),
            (3, 4))
top_column(matrix_2) => 1

matrix_3 = ((3,),
            (4,),
            (9,))
top_column(matrix_3) => 0

matrix_4 = ((-2, -1, -3),)
top_column(matrix_4) => 1
"""


def max_column(matrix):
    max_index = {}
    for i in range(len(matrix)):
        for j, num in enumerate(matrix[i]):
            max_index[j] = 0
            
    for i in range(len(matrix)):
        for j, num in enumerate(matrix[i]):
            max_index[j] += num
    print(max_index)  
    return max(max_index, key=max_index.get)
  
matrix = ((5, 6, 7, 8),
          (3, 9, 2, 5),
          (2, 1, 9, 2))  
print(max_column(matrix))

def top_column(matrix):
    best_sum = None
    best_col = None

    for col in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
          total += matrix[row][col]
        if best_sum is None or total > best_sum:
          best_sum = total
          best_col = col

    return best_col


# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print("All tests passed!")
print("Finished early? Discuss time & space complexity")


"""
NOTES FOR INTERVIEWER

--------- Clarifying questions ---------------

Q: How should I handle invalid input?
A: You can assume the input will be valid.

Q: Is it possible for different rows to have different numbers of elements?
A: You can assume each row will have the same number of elements.

Q: What should I do if two columns are tied for the highest sum?
A: You can assume there will be no ties.

Q: How should I handle an empty matrix?
A: You can assume the matrix will have at least one element.

--------- Hints -------------------------------

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. If they are still unsure, help them to realize that they will need to iterate over the column indices in the outer loop, and the row indices in the inner loop.

- If your candidate forgets to reset their sum for each column, encourage them to print out the total for each column.

"""