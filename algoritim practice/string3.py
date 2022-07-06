# Given a string with parentheses, determine if the sequence is valid. Return true or false. Don't forget your edge cases!


# Example Input: "(In(The)(No(t)To)oDista)ntFuture"
# Example Output: True

# Example Input: "N(ext(Sun)da)yAD)"
# Example Output: False

# Example Input: "(Satt(e(liteOfL(ove"
# Example Output: False

par = "(In(The)(No(t)To)oDista)ntFuture"
def match_par(par):
    d = []
    for i in par:
        if i == '(' or i == ')':
            d.append(i)
    print(d)
    
    a = "".join(d)
    if len(d) %2 != 0:
        return False
    print(a)
    
    while True:
        if '()' in a :
            a = a.replace ( '()' , '' )
        else:
            return not a


print(match_par(par))


# Given a string with different brackets, determine if the sequence is valid. 
# Return true or false. Don't forget your edge cases!
# Example Input: "({In(The)}(No([t)To)oDista]ntFuture"
# Example Output: False

# Example Input: "N{ext([Sun]da)yAD}"
# Example Output: True

# Example Input: "(Satt]e[{lite}OfL(ove)"
# Example Output: False

par1 = "N{ext([Sun]da)yAD}"
def match_par1(par):
    d = []
    for i in par:
        if i == '(' or i == ')'or i == '{' or i == '}' or i == '[' or i == ']':
            d.append(i)
    
    if len(d) %2 != 0:
        return False
    
    a = "".join(d)
    while True:
        if '()' in a :
            a = a.replace ( '()' , '' )
        if '{}' in a:
            a = a.replace ( '{}' , '' )
        if '[]' in a:
            a = a.replace ( '[]' , '' )
        else:
            return not a


print(match_par1(par1))