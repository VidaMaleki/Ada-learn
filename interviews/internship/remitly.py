# Write a function that returns the maximum product of two integers from a list of integers

# For example:

# max_product([100,2,98])    //returns 9800
# possible to have less than 2 nums, negative numbers 
nums = [-10, -12, 3, 7]





def max_product(nums):
    if len(nums) < 2:
        return None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    pos_max_first = nums[-1]
    pos_max_second = nums[-2]
    pos_max = pos_max_first * pos_max_second
    neg_max_first = nums[0]
    neg_max_second = nums[1]
    neg_max = neg_max_first * neg_max_second
    
    if pos_max > neg_max:
        return pos_max
    return neg_max




print(max_product(nums))
assert max_product([100,2,98]) == 9800 
assert max_product([1]) == None 
assert max_product([-3, 3, -5, 7]) == 21
assert max_product([-12, -10, 3, 7]) == 120 
print("All assertions passed!")

# Python program to demonstrate
# main() function
# A = [1,2,3,4,5] and B = [1,9,4,5,6]
# A-B
# [2,3]
# A func which takes two arrays and givesa  diff

#Hello this is Min, the zoom meeting id is invalid. Do you happen to have the correct meeting id?
def main():
  print("hello1!")


  
  
# __name__
if __name__=="__main__":
    main()