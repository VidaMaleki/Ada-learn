# Given an array and a number n,  return the nth-largest number in the array. Don't forget edge cases!

# Example Input: [5, 8, 1, 3, 7, 5, 6], 3
# Example Output: 6

# Example Input: [3, 1, 5], 5
# Example Output: None

arr, n = [5, 8, 1, 3, 7, 5, 6], 3

def nth_largest(arr, n):
    if n > len(arr):
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-n]

print(nth_largest(arr, n))


# Given an array, a start position, and an end position, remove the values within that start-end range, then return the original array. Don't use slice. Don't forget edge cases!

# Example Input: [5, 8, 1, 3, 7, 5, 6,10], 3, 6
# Example Output: [5, 8, 1, 10]

# Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 5,7
# Example Output: [4, 5, 6, 7, 10]

# Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 7,11
# Example Output: [4, 5, 6, 7, 10, 11, 12]

arr1 = [5, 8, 1, 3, 7, 5, 6,10]
start = 3
end = 6

def slice_list(arr1, start, end):
    for i in range(end, start-1,-1):# 6, 2, 
        print(arr1[i])
        arr1.pop(i)
    return arr1
    

print(slice_list(arr1, start, end))