# Given an array of random numbers, decide if one side's sum is equal to the other's. This means it has a balance point between indices. If so, return True, else return False. Don't forget your edge cases!

# Example Input: [ 2, 4, 1, 7 ]
# Example Output: True (2+4+1 = 7)

# Example Input: [ 5, 3, 1, 7 ]
# Example Output: True (5+3 = 1+7)

# Example Input: [ 2, 4, 1, 3, 8 ]
# Example Output: False

arr = [ 5, 3, 1, 7 ]
def balance(arr):
    sum_list = sum(arr)
    if sum_list % 2 != 0:
        return False
    a = 0
    for i in arr:
        if a == (sum_list//2):
            break
        a += i
    if a == (sum_list//2):
        return True
    else:
        return False
            

balance(arr)




# Given an array of random numbers, decide if one side's sum is equal to the other's; 
# however, the balance point is no longer between indices. 
# It's an index. If so, return the index position, else return -1. 
# Don't forget your edge cases!

# Example Input: [ 2, 4, 1, 5, 7 ]
# Example Output: 3 (2+4+1 = 7)

# Example Input: [ 5, 3, 1, 7 ]
# Example Output: -1

# Example Input: [ 10, 10 ]
# Example Output: -1

arr1 = [ 10, 10 ]

def balance_index(arr1):
    sum_list = sum(arr1)
    # if sum_list % 2 != 0:
    #     return -1
    target = sum_list//2
    a = 0
    b = 0
    for i, num in enumerate(arr1):
        a += num
        b = i
        if a == target:
            return -1
        if a > target:
            return b
            

print(balance_index(arr1))