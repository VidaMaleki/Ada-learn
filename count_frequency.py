my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1 ,4, 4, 4, 2, 2, 2, 2]
def CountFrequency(my_list):
    # Creating an empty dictionary
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count


print(CountFrequency(my_list))

