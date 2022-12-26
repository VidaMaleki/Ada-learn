# "SV: You receieve a list of business data from multiple sources with differing priorities. You need to create a result that holds an entry for each business and takes attributes from each of the inputs depending on priority.

# Input = [ {""name"": ""Starbucks"", ""phone_number"": ""12345""},
#     {""name"": ""Starbucks"", ""is_open"": ""true""},
#     {""name"": ""Dunkin"", ""is_open"": ""false""} ] 

# Returns: [{""name"": ""Starbucks"", ""phone_number"": ""12345"", ""is_open"": ""true""}, {""name"": ""Dunkin"", ""is_open"": ""false""} ]"
# "Write a function to tokenize a page of plain text into words (use space as a delimiter) and find out the frequency of occurrence of the words."
# "Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Input: nums = [1,2,1]
# # # Output: [1,2,1,1,2,1]"
# "Given two integer arrays of equal length target and arr. In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps. Return True if you can make arr equal to target, or False otherwise.
# Example 1:
 
# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true"
# "Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters. Letters are case sensitive, for example, ""Aa"" is not considered a palindrome here.
# Example 1:
 
# Input: s = ""abccccdd"" ccdbdcc dccaccd
# Output: 7"
# Write a function to determine whether a word is a palindrome
# "1 - Write a function that takes in an unsorted array of integers and returns the min value and max value.
# 2 - Additionally, return the median value. "
# Problem1: Return duplicates of an array.  Problem 2: Two Sum 
# Two Sum - started with the basic (no need to account for negative or duplicate); once finished, asked how you can change if the input array has duplicates 
# TwoSum - given an array of integers, write a program where the sum of any two integers equals a specified number N.
# No coding question but asked about API's and front end
# Transform a string from "geeks_for_geeks" to "GeeksForGeeks"
# Asked about SQL and instances.
# fibonacci. If you solve it recursively, you will be asked to solve it with hash tables. (may be beneficial to know the memoization and/or iterative solutions, too. different student had to attempt memoization)
# "String concatenation - but presented as though you are recieving packages (libraries). Your algorithm should return the number of packages in the string. The string is a bunch of letters that say things like ""doesntmatterjsutsomepackage.version1.2\nthensomeotherpackage.version2.1\n""   each package in the string is seperated by the \n newline escape. So you just need to return the number of ""\n"" to get the count of packages. The most challenging part about this question was that they talked about packages for a long time - so it was harder to identify that it was just a string concatenation problem. 
# string = ""package1\npackage2\n""
# count = 0

# for i in string:
#   if i == ""\n"":
#     count += 1
# print(count)"
# Given two linked lists, return the sum of the two numbers in the linked lists. For example: [4,5,6] --> 654 and [8,0,1] --> 108. It should return the sum of the two, or 762. 
# Return a sorted list (without using a 'sorted' function.)
# "Define a function that takes an array of numbers (e.g input[]):
#         e.g [1, 2, 3, 4]
# And the function returns an array of numbers that are products of each other number in the array:
# e.g [24, 12, 8, 6]

# iteration 1: 24 is product (all but 1)
# iteration 2: 12 is product (all but 2)
# iteration 3: 8 is product (all but 3)
# iteration 4: 6 is product (all but 4)"
# From an integer that represents a dollar amount. eg. 27 and an array of denominations [20, 10, 5, 1].   Write a function that will return a list of the number of bills you'd need to construct the integer.   input: 27 // output [20, 5, 1, 1]     input: 58 // output [20, 20, 10, 5, 1, 1, 1].
# "Given a string return the most common letter. No need to account for punctuation, capitialization of letters was an edge cast that was okay to work on later. 

# Write a function that will accept two strings as parameters and return True if they are anagrams and False if they are not.

# SV: Write an algorithm to determine whether two strings are anagrams or not."
# Write function that counts number of chars in a str
# You have a string of words or sentences and you have to find the most used word
# "Check if a given string can be rearranged into a palindrome. 

# (I finsished early, Aaron the manager then asked if I can come up with a way to do this only using one for loop. But he's friendly and said at the end he didn't expect me to know the answer, just wanted to use the extra time to discuss)"