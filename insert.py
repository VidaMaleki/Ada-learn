# Replace an empty slice with a list containing the object:

#lst[index:index] = [obj]
# Demo:
lst = [0, 1, 2, 3, 4]

for index in range(len(lst)):
    if index == 2:
        lst[index:index] = [9]
print(lst)
    
# output >>> [0, 1, 9, 2, 3, 4]


# example 2

a = [1,2,3,4,5]
idx = 3
value=[7]

def insert_gen(a,idx,value):
    b=a[:idx] + value + a[idx:]
    return b

final = insert_gen(a,idx,value)
# print(final)

# example 3

def add(lst, obj, index):
    return lst[:index] + [obj] + lst[index:]