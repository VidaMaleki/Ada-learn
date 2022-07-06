# Given an array, reverse the order of values without using the built-in method reverse or slice, 
# ie. [: :-1]. Return the same array. Don't forget edge cases!

# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [6, 5, 4, 3, 2, 1]

arr = [1, 2, 3, 4, 5, 6]
def reverse(arr):
    arr_copy = arr[:]
    for i in range(1, len(arr)+1):
        arr[i-1] = arr_copy[-i]
    return arr


reverse(arr)




# Given an array and number, rotate the values of the array to the right by that number. Don't use slice. Return the same array. Don't forget edge cases!

# Example Input: [1, 2, 3, 4, 5], 2
# Example Output: [4, 5, 1, 2, 3]

# Example Input: [1, 2, 3, 4, 5], 5
# Example Output: [1, 2, 3, 4, 5]

arr1 = [1, 2, 3, 4, 5]
n = 5


def rotate(arr1, n):
    arr1 = [arr1[(i-n)% len(arr1)] for i, x in enumerate(arr1)]
    return arr1


print(rotate(arr1, n))       