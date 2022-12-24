# given a string return the first letter of each word. 
# Input: "Hello, World" output HW  - he just told me the question, it wasnt on replit or given. 

word = "Hello, World"
word = word.split()
initial = ''
for char in word:
    initial += char[0]
print(initial)

# "1. given a list of strings return the duplicates. 
# inputs = [""hi"", ""hi"",""test"",""this""] output: [""hi""] 
# 2. if we altered the problem, how would you then return the word with the highest count 

arr = ["hi", "hi","test","this"] 
count = {}
for i in arr:
    count[i] = count.get(i,0)+1
#1
duplicates = []
for i,j in count.items():
    if j>1:
        duplicates.append(i)
print(duplicates)
#2
print(max(count, key=count.get))

# "Given a list of full names (first and last), return a list of just the first names. 
# If there are multiple people who share the same first name, 
# return the first name with the initial of the last name
# input: ['Nina Lane','Nina Jeong', 'Ada Lovelace', 'Jared Stewart']
# output: [Nina L, Nina J, Ada, Jared]"



# "given a list of nums, print a list of the duplicates that appear in the list"


# "A variation of TwoSum:
# Given an array of integers (both positive and negative) and a target sum, 
# find all unique pairs in the array that add to the sum. 
# EX input: [1, 3, 2, 2, 2, -1, 5, 0, 9, 4, 3, 2], 4
# EX output: {(1, 3), (2, 2), (-1, 5), (0, 4)}
# Output pairs in a set of tuples."


# "### Whole Foods has an app that allows customers to order their groceries online. 
# They would like to add a feature to the app that shows customers how many items they have in their shopping cart. 


# ### Write a method called count_shopping_cart, 
# which takes in a list of items and prints out how many times each item occurs in the list."

# TwoSum

# "Given two strings A and B, output if A is present in B. 
# For ex: if A is “cat"", and B is “carrot” - the output should be true
# if A is “cat” and B is “actor” - the output should be false"


# With two collections of numbers in descending order, 
# write a function that will merge the two and still be sorted in descending order.
# Describle the time complexity of your function.


# Checking if a string is a Palindrome


# The gave a large ingredients list, 
# and a dictionary with the keys being the recipes and the value being a list of ingredients. 
# They wanted you to return a list of the recipes that included all the ingredients you already were given.


# given a string of words, print the first letter of each word. 
# I asked clarifying questions and then wrote short tests to account for edge cases. 
# Input: "the brown fox", output: "tbf"



# Given two lists of integers (A and B) and a number k, 
# return true if a number in A plus a number in B equals K

a = [2, 3, 6, 5, 1]
b = [4,8,6,7,1]
k = 12
def two_sum_list_num(a, b, k):
    
    for i in range(len(a)):
        if (k - a[i]) in b:
            return True
    return False

print(two_sum_list_num(a, b, k))

# - Given two lists, return a list that contains their intersecting values.


# FizzBuzz
# 
# 
# You are given an array of integers. 
# Find the starting index of the triplet that sums to the largest value. 
# A triplet is defined as a sequence of three consecutive values within the array.

a = [7,2,3 ,4, 8, 6, 9]


def triplet_sum(a):
    max_num = max(a)
    triple = []
    for i in range(1,len(a)):
        if (a[i-1]+a[i]+a[i+1]) == max_num:
            return i-1
    return None
        
    
print(triplet_sum(a))
#max-num - num=     
    
# "Amazon is having a site-wide sale; everything is 20% off. 
# Can you write me a function that takes a sentence found on the Amazon retail website, 
# discounts the price if there is a price present, and finally returns the modified sentence.



# Example: ""Amazon Echos are $50 today."" > ""Amazon Echos are $40 today.""
# "