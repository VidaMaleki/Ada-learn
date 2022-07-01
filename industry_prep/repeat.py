'''
Your goal is to find the first character repeated less than a given number of times in a data structure.

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

Your function will recieve a matrix and an integer n where n>1. Our goal is to find the first character when iterating row-wise that shows up in the matrix strictly fewer than n times.

For example, take matrix_1 and n=3. We see that, 'u' is repeated 3 times and 'e' is repeated 4 times. However, 'r' appears only 2 times. 'r' is thus the first character when iterating row-wise to appear fewer than n times. The function should return 'r' in this case.

See the tests for more examples.
'''
def first_uncommon(matrix, n):
    freq = {}
    for row in matrix:
        for letter in row:
            if letter not in freq:
                freq[letter] = 0
            freq[letter] += 1

    for row in matrix:
        for letter in row:
            if freq[letter] < n:
                return letter

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n'),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r'),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert first_uncommon(matrix_1, 2) == 'd'
assert first_uncommon(matrix_1, 3) == 'r'
assert first_uncommon(matrix_1, 4) == 'u'

matrix_2 = (
    ('💜'),
)
assert first_uncommon(matrix_2, 2) == '💜'
assert first_uncommon(matrix_2, 525600) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")
"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if none of the strings meet the criteria?
A: You can assume there will be at least one string that meets the criteria.

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

Q: Can n be less than 2?
A: Also no.

Q: 💜?
A: 💜

--------------------------------------------------


---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

 - If your candidate is concerned about the complexity of multiple double for-loops, encourage them to not worry about the complexity and just focus on a working solution.

 -------------------------------------------------
"""