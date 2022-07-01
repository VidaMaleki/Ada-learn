'''
Your goal is to find a hidden message in a data structure.

The data structure will be a ragged matrix, represented by a tuple of tuples of strings. Each string will be a single character, but each inner tuple may have a different length. For example:

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n'),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r'),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)

Your function will recieve a matrix and a positive integer n. The integer n represents how frequently to select characters from the matrix.

Your code should iterate over the matrix row-wise and create a string containing every nth character from the iteration. For example, with the above matrix and an n of 2, the first character of the result string should be 'u', then 'r', then ' ', then 'd', and so on.

For this example of matrix_1 and n=2, the secret message is 'ur doing great'. See the tests for more examples.
'''

def hidden(matrix, n):
    letters = []
    i = 0
    for row in matrix:
        for letter in row:
            if i % n == 0:
                letters.append(letter)
            i += 1
    return ''.join(letters)

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n'),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r'),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜'),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")



"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if there is invalid input?
A: You can assume the input will be valid.

Q: What should I do if matrix is empty?
A: You can assume the matrix will have at least one string.

Q: Can a string have multiple characters?
A: No.

Q: Does case matter?
A: Yes, 'a' and 'A' should be considered different.

Q: Will there be any empty inner tuples?
A: No.

Q: Can n be less than 1?
A: Also no.

Q: Am I really doing great?
A: Yes 💜

--------------------------------------------------


---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

 - If your candidate is concerned about the complexity of a double for-loop, encourage them to not worry about the complexity and just focus on a working solution.

 -------------------------------------------------
"""