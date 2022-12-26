"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input will have exactly one solution, and you may not use the same element twice.

Return the answer in a list with the smaller index first.

Example: 
Input: nums = [3,7,11,15], target = 9
Output: [0,1]

credit: https://leetcode.com/problems/two-sum/

"""
# mydict = {'george': 16, 'amber': 19}
# print mydict.keys()[mydict.values().index(16)]  # Prints george
#a = car["year"]
# x =[ e for e,b in car.items() if b==a ]

def two_sum(nums, target):
    answer = []
    required = {}
    for i , num in enumerate(nums):
        pair = target - num 
        if pair in required:
          answer.append([required[pair],i])
        else:
          required[num]=i
    print(required)
    return answer     

print(two_sum([2,7,11,15], 9))

# assert two_sum([2,7,11,15], 9) == [0, 1]
# assert two_sum([5,7,3,15], 22) == [1, 3]
# assert two_sum([1, 2], 3) == [0, 1]