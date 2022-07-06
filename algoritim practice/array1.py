# Given an array, swap every pair of successive values and return the array.
# Don't forget your edge cases!

# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [2, 1, 4, 3, 6, 5]

# Example Input: [True, "a", 1]
# Example Output: ["a", True, 1]

# TRY TO MODIFY THE ORIGINAL ARRAY

array = [1, 2, 3, 4, 5, 6]

def switch_pair(array):
    new_array = []
    for i in range(1,len(array),2):
        new_array.append(array[i])
        new_array.append(array[i-1])
        if len(array) %2 != 0:
            new_array.append(array[i+1])
    return new_array    
    
        
print(switch_pair(array))    



# Someone accidentally duplicated the data found in an array. 
# We need you to remove all duplicate values in a sorted array, then return the array. 
# Don't forget your edge cases! TRY TO MODIFY THE ORIGINAL ARRAY

# Example Input: [1, 2, 2, 3, 5, 6, 6, 6, 8]
# Example Output: [1, 2, 3, 5, 6, 8]

# Extra Challenge

# Example Input: ["a", "a", "b", "c", "c", "c", "d", "d"]
# Example output: ["a", "b", "c", "d"]

array2 = [1, 2, 2, 3, 5, 6, 6, 6, 8]
def remove_duplicate(array2):
    new_array = []
    for i in range(len(array2)):
        if array2[i] in new_array:
            continue
        else:
            new_array.append(array2[i])
    return new_array

print(remove_duplicate(array2))


#Remove any duplicates from a List:

mylist = [1, 2, 2, 3, 5, 6, 6, 6, 8]

mylist = list(dict.fromkeys(mylist, 0))

print(mylist)