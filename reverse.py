# example 1
a = "hello"
a = list(a)
b = []
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print("".join(b))


# example 2
def reverse_string(s):
    l,r = 0, len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r -1
    return s
        
        
        
# example 3        
def reverseString(s):
    stack = []
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i +=1
    return s