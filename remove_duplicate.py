#Remove any duplicates from a List:

#First we have a List that contains duplicates:
mylist = [1, 2, 2, 3, 5, 6, 6, 6, 8]
# Create a dictionary, using the List items as keys. 
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.

# Then, convert the dictionary back into a list:
mylist = list(dict.fromkeys(mylist))
print(mylist)

nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    
    
    nums[:]=list(dict.fromkeys(nums))
    return nums

print(removeDuplicates(nums))