# Question: Given two arrays, find and return the number(s) which are present in the first array but are not present in the second array.

# Array1: 1,2,3,4,5
# Array2: 2,3,1,0,5 

# Result: [4]

# Array1: 1,2,3,4,5,10
# Array2: 2,3,1,0,5 

# Result: [4,10]

# initialize an empty list variable
# use a set to store everything in the second array
# iterate through the first array (in cases of many repeated numbers, could consider converting it to a set first) and just check if the number is found in the second array-set
# append number to return list if not found in second array-set
# end of for loop, check length of return list and return it if >=1 otherwise return "No unique numbers"

def unique_nums_in_first_arr(arr1, arr2):
    unique_nums = [] # O(N) space complexity
    second_set = set(arr2) # 0(N) time/space complexity
    for num in arr1:
        if num not in second_set: # 0(1) time complexity
            unique_nums.append(num) # O(1) time complexity
    return unique_nums if len(unique_nums) >= 1 else "No unique numbers found"

assert unique_nums_in_first_arr([1,2,3,4,5], [2,3,1,0,5]) == [4]
assert unique_nums_in_first_arr([1,2,3,4,5,10], [2,3,1,0,5]) == [4,10]
assert unique_nums_in_first_arr([1,2,3,5], [2,3,1,0,5]) == "No unique numbers found"
assert unique_nums_in_first_arr([],[]) == "No unique numbers found"



class Validation:
    def __init__(self):
        console.log()



class ValidInt(Validation):
    pass
    
    
    
    
    
#retail assistant 
'''
You are an awesome intern and want to give your coworkers some cookies. While you should only give each coworker one cookie, some coworkers will only accept big cookies.
#

Each cookie has a size, stored in a size array. Each cookie j has a size s[j].

Each coworker i has a greed factor. g[i] is the minimum size of a cookie that they will be content with. 

If s[j] >= g[i], we can give the cookie j to i, and the coworker i will be content. Your goal is to maximize the number of content coworkers and output the maximum number.

cookie_size = []
Will accept cookie >= greed factor 

Example 1:
=
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 coworkers and 2 cookies. The greed factors of 3 coworkers are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the coworker whose greed factor is 1 content.
You need to output 1.
Example 2:
'''