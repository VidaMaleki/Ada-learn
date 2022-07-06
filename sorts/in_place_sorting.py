my_list = [4, 2, 3, -1, -2, 0, 1]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):

        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)


#sort without range and append
a = [3, 1, 5, 2, 4]

for i in a[1:]:
    j = a.index(i)
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
    j = j - 1

#Taking a list from the user and then sort it.

n = int(input("List length = "))
list1 = []

for i in range(n):
    x = int(input("Elements  (0 a 9) = "))
    if (i == 0) or (x > list1[- 1]):
        list1.append(x)
    else:
        pos = 0
        while pos < len(list1):
            if x <= list1[pos]:
                list1.insert(pos, x)
                break
            pos = pos + 1

print(list1)


#sort without built-in functions
# example -1 
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)

# example -2 
NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)

# example - 3


data_list1 = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list1 = []

while data_list1:
    minimum = data_list1[0]  # arbitrary number in list 
    for x in data_list1: 
        if x < minimum:
            minimum = x
    new_list1.append(minimum)
    data_list1.remove(minimum)    

print(new_list1) 