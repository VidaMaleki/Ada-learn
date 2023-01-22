
s = "   -4193 with words"
def str_to_int(s):
    trimed_s = s.strip()
    sign = ['-', '+']
    get_sign = ""
    answer = ""
    for char in trimed_s:
        if trimed_s[0] in sign:
            if char == '-':
                get_sign += "-"
            continue
        if char.isnumeric() == True:
            answer += char
        break
    print(answer)
    if get_sign == "-":
        return -int(answer)
    return int(answer)   
                
        
print(int("2345"))  
# print(str_to_int(s))
trimed_s = s.strip()
answer = ""
for i in range(len(trimed_s)):
    if i.isnumeric()
    answer += i
    
print(answer)