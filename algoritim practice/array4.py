# Given two arrays, create your own concatenation function. Return a new array containing the first array's values, then the second array's values. Try not to use built-in methods.  Don't forget edge cases!

# Example Input: ["a", "b", "c"], [1, 2, 3]
# Example Output: ["a", "b", "c", 1, 2, 3]
arr1, arr2 = ["a", "b", "c"], [1, 2, 3]

def concat_lists(arr1, arr2):
    return arr1 + arr2

def concat_sum(arr1, arr2):
    return sum((arr1, arr2), [])

print(concat_lists(arr1, arr2))
print(concat_sum(arr1, arr2))

# Given an array, find the smallest value and move it to the front of the array. Return the same array. Try not to use built-in methods. Don't forget edge cases!

# Example Input: [3, 4, 2, 9, 1, 8, 7, 6]
# Example Output: [1, 3, 4, 2, 9, 8, 7, 6]

# Example Input: [3, 4, 2, 9, 1, 8, 1, 7, 6]
# Example Output: [1, 3, 4, 2, 9, 8, 1, 7, 6]
arr = [3, 4, 2, 9, 1, 8, 7, 6]

def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
            
    for num in arr:
        if smallest in arr:
            arr.remove(smallest)
            arr.insert(0, smallest)
    return arr


print(find_smallest(arr))