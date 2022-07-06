# Given an array of sorted page numbers, return a string of the page ranges. Any consecutive numbers should be hyphenated. Don't forget your edge cases!

# Example Input: [1,3,5,6,7,9,10,12]
# Example Output: "1, 3, 5-7, 9-10, 12"
arr = [1,3,5,6,7,9,10,12]

# def consecutive_numbers(arr):
#     answer = []
#     len_arr = max(arr) +1
#     for i in range(1, len_arr):
#         a = i-1
#         if arr[i-1] == i-1  and arr[i] == i:
#             answer.append(f'{a}-{arr[i]}')
#         else:
#             answer.append(f'{a}, ')
#     return answer       

# consecutive_numbers(arr)

# Given two arrays, return a dictionary using the first array as keys and the second array as the values. Don't forget your edge cases!

# Example Input: 
# [ "name", 222, "moon" ], [ False, "abc", 123 ]
# Example Output: 
# {"name": False, 222: "abc", "moon": 123 }

# Example Input: 
# [ "name", 222, "moon" ], [ "abc", 123 ]
# Example Output: 
# {"name": "abc", 222: 123, "moon": None }

# Example Input: 
# [ "name", 222 ], [ False, "abc", 123 ]
# Example Output: 
# None
arr1 = [ "name", 222, "moon" ]
arr2 = [ False, "abc", 123 ]
def combine_dict(arr1, arr2):
    combine = {}
    for i in range(lenarr1:
        combine[i] = arr2[i]
    print(combine)
    return combine

print(combine_dict(arr1, arr2))

# Given a dictionary, reverse the values and keys and return a new dictionary. Don't forget your edge cases!


# Example Input: 
# {"name": False, 222: "abc", "moon": 123 }
# Example Output: 
# {False: "name", "abc": 222, 123: "moon" }



