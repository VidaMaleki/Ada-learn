# Write a solution to the Buying Stock function below. The following tests will evaluate your solution.

# Tests converted to Pytest


def max_profit(arr):
    if arr == [] or len(arr) ==1:
        return 0
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

    

def test_profit_7_1_5_3_6_4(self):
    # Arrange
    arr = [7, 1, 5, 3, 6, 4]

    # Act
    answer = max_profit(arr)

    # Assert
    assert answer == 7

def test_profit_1_2_3_4_5(self):
    # Arrange
    arr = [1, 2, 3, 4, 5]

    # Act
    answer = max_profit(arr)

    # Assert
    assert answer == 4

def test_profit_7_6_4_3_1(self):
    # Arrange
    arr = [7, 6, 4, 3, 1]

    # Act
    answer = max_profit(arr)

    # Assert
    assert answer == 0