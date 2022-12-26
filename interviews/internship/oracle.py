# name = input('What is your number?\n')
# print('Hi, %s.' % name)



# number = input('What is your number?\n')
# print('Hi, %s.' % number)


# #get user input as a number
# #create fibonacci seq up to that number given
# # 0, 1, 1, 2, 3, 5, 8
# # num[i + j]
# #create a return list value that holds the first iteration value
# #and previous one, to add up to next number 
# #then append that value to my fibonacci sequence list
# fib_list = []
# first_num = 0
# last_num = 0 
# def fibonacci_seq(num):
#     user_input_number = int(num)
#     for number in user_input_number:
#         add = first_num[number] + last_num[number]
#         fib_list.append(add)
        
# print(fibonacci_seq(5))
        
 
    
# def fibonacci(n, arr):
#     a = 0
#     b = 1
#     # Check is n is less
#     # than 0
#     if n < 0:
#         print("Incorrect input")

#     # Check is n is equal
#     # to 0
#     elif n == 0:
#         return 0

    # # Check if n is equal to 1
    # elif n == 1:
    #     return b
    # else:
    #     for i in range(1, n):
    #         c = a + b
    #         a = b
    #         b = c
        
    # return b

# Driver Program
# print(fibonacci(6, arr))


# def Fibonacci(n):
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# # Driver Program
# print(Fibonacci(9))

FibArray = [0, 1]
 
def fibonacci(n):
   
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:       
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]
 
# Driver Program
print(fibonacci(9))


def multi(num):
    if num == 0:
        return 1
    if num < 0:
        raise ValueError("Inavalid input: input must be greater than zero")
    return num * multi(num-1)


# 5*4*3*2*1 = 120

print(multi(5))