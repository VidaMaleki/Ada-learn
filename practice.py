# # list(map(len, words))
# # [len(word) for word in words]


# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))
# #[2, 4, 6, 8]


# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))
# #[5, 7, 9]

# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']

# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
# #[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]



# a = ['a', 'b', 'c']
# b = [1, 2, 3, 0]
# x = dict(zip(a,b))
# if all(b):
#     print("YES ALL True")
    
# def checkString(s):
#     s_dict = {}
#     for x in s:
#         s_dict[x] = s_dict.get(x, 0) +1
#     print(s_dict)
    
#     if "a" in s:
#         len_a = s_dict['a']
#         if s[:len_a] == ('a' * len_a):
#             return True
#     elif "a" not in s and s != '':
#         return True
        
#     return False

# print(checkString("bbb"))



# # Write a function that will take two lists of integers (representing “blids”): a “pre-image” and “post-image”, and return the list of blids that should be deleted (i.e., they appear in the pre-image but not in the post-image).

# # Example:
# # preImage = [42, 32, 45, 43, 23, 90, 87, 36]
# # postImage = [23, 36, 90, 45]

# # Method should return the list : [32, 42, 43, 87]
# preImage = [42, 32, 45, 43, 23, 90, 87, 36]
# postImage = [23, 36, 90, 45]



# def ddd(preImage, postImage):
#     new_list = []
#     for i in range(len(preImage)):
#         if preImage[i] not in postImage:
#             new_list.append(preImage[i])
#     return new_list


# print(ddd(preImage, postImage))

s = "loveleetcode"

def countFrequency(s):
    s_dict = {}
    splitted_s = list(s)
    print(splitted_s)
    for char in splitted_s:
        s_dict[char] = s_dict.get(char, 0)+1
        
    print(s_dict)
    answer= ""
    for k, v in s_dict.items():
        if v == 1:
            answer=k
            break
    
    for i, char in enumerate(splitted_s):
        if char == answer:
            return i
        
print(countFrequency(s))