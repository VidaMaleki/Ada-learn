#Tom Servo's been collecting pennies for years,
# but he's running out of space in his room! 
# Create a function for him that will turn his pennies into the smallest number of coins. 
# Think quarters, dimes, nickels, pennies. 
# Example Input: 174
# Example Output: 
# "Quarters: 6
#  Dimes: 2
#  Pennies: 4"

# num = 174

def num_converter(num):
    q = num // 25
    d = (num %25) // 10
    p = ((num%25)%10) //1
    print(f'q: {q}')
    print(f'd: {d}')
    print(f'p: {p}')
    
num_converter(174)


# Given a number, continuously sum that number until it is one digit.

# Example Input: 477
# Example Output: 9

# How did I get 9???

# Example Input: 246
# Example Output: 3

def str_num(num):
    str_num = str(num)
    list1 = []
    for i in str_num:
        list1.append(int(i))
    answer1 = 0
    for i in range(len(list1)):
        answer1 += list1[i]
    return answer1

def sum_num(num):
    list1 = str_num(num)
    if list1 > 9:
        list1 = str_num(list1)
    return list1

sum_num(477)

#second solution
def to_one_digit(num):
    digit = helper(num)
    while digit > 9:
        digit = helper(digit)
    return digit

def helper(num):
    digit = 0
    while num > 0:
        digit += num % 10
        num = num // 10
    return digit


to_one_digit(477)


# You work for a company that makes retro terminal games.
# Your job is to create title cards with text, spaces, and stars, like so:

# ******************************
# ||         WELCOME          ||
# ******************************

# Given a "title" (a string), center it in the title card! There's some limitations, though.
# You only have 75 characters per line. 
# What happens if the title is longer than 75? Well, get creative!


title = "Vida"
def welcome_title(title):
    print_title = list('||                          ||')
    start = (len(print_title) //2) - (len(title) //2)
    end = start + len(title)
    print_title[start:end] =  title
    print("******************************")
    print("".join(print_title))
    print("******************************")
    


welcome_title(title)    
