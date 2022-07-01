# Write a function factorial that accepts an integer parameter n. It uses recursion to compute and return the value of n factorial (also written as n!).

# Here are the tests:

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Inavalid input: input must be greater than zero")
    return factorial(n -1) * n 




def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive_num():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1


def test_factorial_negative_num():
    with pytest.raises(ValueError):
        factorial(-1)