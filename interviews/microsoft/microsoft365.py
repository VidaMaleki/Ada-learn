def isValid(s):
    
  stack = []
  for ch in s:
    if ch in ["(", "{", "["]:
      stack.append(ch)
    else:
      if not stack:
        return False
      curr = stack.pop()
      if ch == "(":
        if curr != ")":
          return False
      if ch == "{":
        if curr != "}":
          return False
      if ch == "[":
        if curr != "]":
          return False
        

#   if stack:
#     return False

      
#   return True

# print(isValid("(())"))
# print(isValid("["))
# print(isValid("{}[]()"))
# print(isValid("((})"))


# You are given a string s that contains a combination of the following characters:

# [ ] { } ( ) 

# Determine if the input string is valid, based on the following criteria:
#   - Open brackets must be closed by the same type of brackets.
#   - Open brackets must be closed in the correct order.

# --
# Example 1:

# Input: s = "()"
# Output: true
# --
# Example 2:

# Input: s = "()[]{}"
# Output: true
# --
# Example 3:

# Input: s = "(]"
# Output: false
# --
# Example 4:

# Input: s = "([)]"
# Output: false
# --

# Constraints:
#   -   1 <= s.length <= 104
#   -   s consists of parentheses only '()[]{}'.