# Given a string, reverse it, and return a new string. Do not use the built-in function reverse.  Don't forget your edge cases!


# Example Input: "pineapple"
# Example Output: "elppaenip"


# Extra Challenge

# Remember, string concatenation is O(n^2). Do some research and find a way to make it more efficient.

word = "pineapple"
d = list(word)
print(d)
w = ""
for i in range(len(d)-1, 0, -1):
    w += d[i]
print(w)




# Given an array of strings, remove any strings that are of equal length, and return the original array. 
# Work in-place. Don't forget your edge cases!

# Feel free to use remove since we've built something similar in the past.

# Example Input: 
# [ "Somewhere", "in", "time", "and", "space" ]
# Example Output: 
# [ "Somewhere", "in", "time", "and", "space" ]

# Example Input: 
# [ "Hot", "blooded", "check", "it", "and", "see" ]
# Example Output: [ "blooded", "check", "it"]


str_list = [ "Hot", "blooded", "check", "it", "and", "see" ]

s = {}
for i, num in enumerate(str_list):
    s[len(num)] = s.get(len(num), 0)+1
print(s)
q = []
for i, j in s.items():
    if j == 1:
        q.append(i)
print(q)    
answer = []
for i in str_list:
    if len(i) in q:
        answer.append(i)
print(answer)
