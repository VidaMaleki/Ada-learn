my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1 ,4, 4, 4, 2]
def CountFrequency(my_list):
    # Creating an empty dictionary
    count = {}
    for num in my_list:
        count[num] = count.get(num,0) +1
    return count

def unique_duplicates(my_list):
    frequency = CountFrequency(my_list)
    count_num = 0
    for v in frequency.values():
        if v >1:
            count_num +=1
    return count_num

print(unique_duplicates(my_list))

