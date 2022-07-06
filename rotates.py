

test_list = [1, 4, 6, 7, 2]
# rotate from left
test_list = [test_list[(i + 3) % len(test_list)]for i, x in enumerate(test_list)]
# List after left rotate by 3 : [7, 2, 1, 4, 6]

# rotate from right
test_list = [test_list[(i - 3) % len(test_list)]for i, x in enumerate(test_list)]

# List after right rotate by 3: [6, 7, 2, 1, 4]

# test_list i= 0 >>> (0+ 3) % 5 = 3 >>> test_list[3] = 7
# 0 * 5 + 3 = 3 >>>
# 0 * 5 + 4 = 4 >>>
# 0 * 5 + 5 = 0 >>>
# 0 * 5 + 6 = 1 >>> 
# 0 * 5 + 7 = 2 >>>                   
# test_list i= 1 >>> (1+ 3) % 5 = 4 >>> test_list[4] = 



#example 2
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


#example 3
def rotate_list(arr, m):
    index = len(arr) - (m% len(arr))
    arr[index:], arr[:index]= arr[:index], arr[index:]

#example 4
nums = [1,2,3,4,5,6,7] 
k = 3
class Object:
    
    def rotate(self,nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [nums[(i+k)% len(nums)] for i, x in enumerate(nums) ]
        return nums

d = Object()
print(d.rotate(nums, k))