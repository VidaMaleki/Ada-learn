def isPalindrome(s):
        return s == s[::-1]
    
def longestPalindrome(s):
    if not s:
        raise Exception("You werent supposed to be null")
        
    if isPalindrome(s):
        return s
            
    for i in range(len(s), 0, -1):
        for j in range(0, len(s)-i+1): 
            candidate = s[j:j+i]
            if isPalindrome(candidate):
                return candidate
            
print(longestPalindrome(s))           



"""        111
 0123456789012
"Hey ,sis, yeh"
first >>> reverse loop i = 13 ,0   second >>> loop j = 0, 13 - i+1
i = 13  j=0 0,(13-13+1) = 1     >>> s[0:0+13]
    12    0     >>>  12    1
    11 : 0         11   :   1       11   :   2
    
"""           

s= "Hey ,sis, yeh"
print(len(s))
# Example Output: "ey, sis, ye"

# s="racecars are great!"
# Example Output: "racecar"

# s="summer love"
# Example Output: "mm"      
            
