# Given two strings, return "G" if the values at the same index match, or "B" if they don't. 
# EX Input: "CRATE", "GRATE"
# EX Output: "BGGGG"
# EX Input: "CRATE", "SOARE"
# EX Output: "BBGBG"

# After solving this, was asked to return "Y" if the value was in the other word, but just not at the same index
# EX Input: "CRATE", "SOARE"
# EX Output: "BBGYG"

# After solving this, was asked to return an int that represents how many index values that letter is from the it's place in the first string. 
# EX Input: "CRATE", "SOARE"
# EX Output: "BBG2G"
word1, word2 = "CRATE", "GRATE"

def matching_index(word1, word2):
    x = list(word1)
    y = list(word2)
    a = ""
    for i, char in enumerate(x):
        if x[i] == y[i]:
            a += 'G'
        else:
            a += 'B'
    return a

print(matching_index(word1, word2))


# Same as above, but we had extra time, so she also asked the following question:

# Given a number, N, print all combinations of A/B where A is between 0 & N and B is between 1 & N
# For example:
# N = 1, output: {0/1, 1/1}
# N = 2, output: {0/1, 1/1, 1/2, 2/2}
# N = 3, output: {0/1, 1/1, 1/2, 1/3, 2/2, 2/3, 3/3}

# Then, an additional restraint was added where fractions with the same simplified values should not be added.
# For example:
# N = 3, output: {0/1, 1/1, 1/2, 1/3, 2/3} because 2/2 simplifies to 1/1 and 3/3 also simplifies to 1/1.
n = 2

a = set()
for i in range(0,n+1):
    for j in range(1,n+1):
        a.add(f'{i}/{j}')
        if i == j:
            a.add(f"{1}/{1}")
print(a)





# Output the Farey sequence of order N, where N is provided as input. 
# The Farey sequence of order N is a sequence of completely reduced fractions between 0 and 1,
# sorted in increasing order such that the denominators are <= N and 
# all numbers are in reduced forms, e.g. 4/4 will be reduced to 1/1.
# Example I/O: 
# (0, 1) = 0/1, 1/2, 1/1
# (0, 1, 2) = 0/1, 1/3, 1/2, 2/3, 1/1
# (0, 1, 2, 3) = 0/1, 1/2, 1/3, 1/4, 2/3, 3/4, 1/1





# "Leetcode#73given a matrix of integers - mat[row][col]
# write a function that will update every entry which shares a row or column with a ""0"" to ""0""
# Example:
# Input:{{0, 1, 2}, {3, 4, 5}}         
# Output:{{0, 0, 0}, {0, 3, 5}} 

# *The prompts/ hints/ redirects were communicated in C## which was a little confusing*"
matrix = [[1,1,1],[1,0,1],[1,1,1]]
#        [[1,0,1],[0,0,0],[1,0,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#          [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
def set_zeros(matrix):
    b = []
    for i in range(len(matrix)):
        for j, num in enumerate(matrix[i]):
            
            if num == 0:
                b.append(j)
                matrix[i] = [0 for x in matrix[i]]
                print(matrix)
    for i in range(len(matrix)):
        for j , num in enumerate(matrix[i]):
            if j in b:
                matrix[i][j] = 0
        
    return matrix


print(set_zeros(matrix))




# "Write a function which takes an input of a string that reverse the words of the sentence e.g. 
# ""Today is 3rd Thursday of Month"" Output: ""Month of Thursday 3rd is Today""
# Follow-up question: Account for multiple spaces in string ""Cat   in the hat"" => ""hat the in   Cat"""

def reverse_sentence_word(sentence):
    pass




# "1. Given a string, determine if it is a palindrome. Spaces and punctuation should be checked the same as the characters. Letter case does not matter. Return true if it is a palindrome, or false if not

# Input: ""ad a""
# Output: false

# Input: ""Ada""
# Output: true
# "




# "given a string and a forbidden letter, remove that forbidden letter from the string IN PLACE.
#   ex: ""dog"" & ""o"" => ""dg""
#   ex: ""cat"" & ""d"" => ""cat""
#   ex: ""doggy"" & ""g"" => ""doy"""




# 1. Reverse a string, "hello" so that it returns "olleh" 
a = "hello"
a = list(a)
b = []
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print("".join(b))



# 2. Drew a picture of stick figures in a line. Assume they're all holding hands. 
# (Wants you to ask about data type - she says to assume they're in an array). 
# Write a method to remove the nth person from the line.
# 0  0  0  0  0 
#/|\/|\/|\/|\/|\
#/ \/ \/ \/ \/ \
head = '  0 '
body = '//||\\'
def add_person(head, body, leg):
    pass
# 3. Now assume those people are in a linked list. 
# How would you change your code to remove the nth person from the array? 
# 4. Reverse words in a sentence ex: "good morning" => "morning good"






