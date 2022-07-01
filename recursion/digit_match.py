# Write a recursive function named digit_match. It accepts two non-negative integers as parameters. It returns the number of digits that match in the two integers.

# Two digits match if they are equal and have the same position relative to the end of the number (i.e. starting with the ones digit).

# In other words, the function should compare the last digits of each number, the second-to-last digits of each number, the third-to-last digits of each number, and so fort, counting how many pairs match.

# Example:

# First number: 1072503891
# Second number: 62530841
# Number of matches: 4
# Matching pairs: 2-2, 5-5, 8-8, 1-1
# 1 0 7 2 5 0 3 8 9 1
#     | | | | | | | |
#     6 2 5 3 0 8 4 1


def digit_match(num1, num2):
    num1, num2 = str(num1), str(num2)
    
    count = 0
    if not num1 or not num2 :
        return count = 0
    elif num1[-1:] == num2[-1:]:
        return count +=1
    return digit_match(num1[-1:], num2[-1:])



def test_digit_match_large_inputs():
    apples = 1072503891
    oranges = 62530841

    assert digit_match(apples, oranges) == 4


def test_digit_match_no_matches():
    apples = 0
    oranges = 62530841

    assert digit_match(apples, oranges) == 0


def test_digit_match_clustered_matches():
    apples = 841
    oranges = 62530841

    assert digit_match(apples, oranges) == 3


def test_digit_match_single_digits():
    apples = 0
    oranges = 0

    assert digit_match(apples, oranges) == 1


def test_digit_match_small_inputs():
    apples = 10
    oranges = 20

    assert digit_match(apples, oranges) == 1