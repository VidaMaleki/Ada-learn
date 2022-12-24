# Write a function that given an array of integer numbers
# and an integer target, return indices of the two numbers such
# that they add up to the target.
# You may assume that each input would have exactly
# one solution, and you may not use the same element twice.

#hash key: num to find value: index 7:0
'''
input arr
output [i1, i2]
if no answer =[]
map key number val=index

'''
 
def twosum(input, target):#time O(n) space O(n)
    my_map={}
    for i in range(len(input)):
        current=input[i]
        pair_num=target-current
        if pair_num in my_map:
            return [my_map[pair_num], i]
        else:
            my_map[input[i]]=i
    return None

if __name__ == "__main__":
   print(twosum([2,7,11,15],9)) # [0,1]
   print(twosum([3,3],6))       # [0,1]
   print(twosum([3,2,4],6))     # [1,2]