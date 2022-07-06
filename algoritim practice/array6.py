# Given a nested array, "flatten" the array, so that all values are in a one-dimensional array. Feel free to return a new array. Don't forget your edge cases!

# Example Input: [ 1, [ 2, 3 ], 4, [ ] ]
# Example Output: [ 1, 2, 3, 4 ]

# Example Input: [ 1, [ 2, 3 ], 4, [ 5, 6, 7 ] , [ 8 ] ]
# Example Output: [ 1, 2, 3, 4, 5, 6, 7, 8 ]

# Now, try "flattening" in-place

arr = [ 1, [ 2, 3 ], 4, [ ] ]

def flattening(arr):
    q = []  
    for i in arr:
        if isinstance(i,list):
            q= q+i
        else:
            q.append(i)
    return q
            
print(flattening(arr))


# Given an array with random numbers, remove duplicates. 
# Return a new array. Don't forget your edge cases!

# Example Input: [ 1, 2, 1, 5, 1, 1, 3 ]
# Example Output: [ 1, 2, 5, 3 ]

# Now, try removing duplicates in-place


arr1 = [ 1, 2, 1, 5, 1, 1, 3 ]
a = list(set(arr1))
print(a)

def remove_duplicates(arr1):
    
    q = {}
    for i in arr1:
        q[i] = q.get(i,0)+1
    return list(q.keys())
    
    
print(remove_duplicates(arr1))