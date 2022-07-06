# Given an array and a value, append the new value to the front of the array. 
# Do not use any built-in array methods, like insert, shift, slice [:], etc. 
# Do this manually. You can use len, pop, append. Return the same array. Don't forget edge cases!

# Example Input: [1, 2, 3, 4, 5, 6], 10
# Example Output: [10,1, 2, 3, 4, 5, 6]

arr = [1, 2, 3, 4, 5, 6]
n= 10


def add_to_front(arr, n):
    arr.append(n)
    for i in range(len(arr)-2, 0,-1):
        arr[i+1] = arr[i]
        arr[i] = arr[i-1]
    arr[0] = n    
    return arr

print(add_to_front(arr, n))



# Given an array, a value, and an index position, insert the new value at the designated position. Do not use any built-in array methods. Return the same array. Don't forget edge cases!

# Example Input: [1, 2, 3], 4, 1
# Example Output: [1, 4, 2, 3]

# EXTRA CHALLENGE

# Example Input: [1, 2, 3, 4, 5], 6, 7
# Example Output: [1, 2, 3, 4, 5, None, None, 6]

arr = [1, 2, 3]
n = 4
m = 1
def insert_n(arr, m, n):
    arr.append(n)
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
        if i == m:
            arr[i] = n
            break
        else:
            arr[i]: arr[i-1]
    return arr

print(insert_n(arr, m, n))    







# Seems like a lot of duplicate code. How could we modify add_to_front so we can use it as a helper function for insert? 
