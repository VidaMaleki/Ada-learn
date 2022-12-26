"""
A Palindrome is a phrase or a word that can spelled the same way forwards and backwards regardless of punctuation

Classic Palindromes: 
1. Race car
2. A man, a plan, a canal ... Panama!

Write a function that determines if a string is a Palindrome

"""
#ignore case, punctuation, spaces 
#aaaaaaaaaaaaaa yes
#"" no 
#return boolean value 

def determine_palindrome(s):
  #initialize a new string 
  #append each char in s to the new string in reverse
  #check for a match
  #if reversed string and original string s match, return true
  #else return false
  reverse= ""
  forwards=""
  for char in s:
    if char.isalpha():
      reverse = char + reverse #R 
      forwards = forwards + char 
    #appending each character to the end of the reversed string
  if forwards.lower() == reverse.lower(): 
    return True
  else: 
    return False 

print(determine_palindrome("A man, a plan, a canal ... Panama!"))


