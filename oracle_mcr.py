

def build_counts(string):
    ctr = {}
    for c in string:
        ctr[c] = ctr.get(c, 0) + 1
    return ctr
print(build_counts("arrc"))
def anagram(string1, string2):
    if string1 != string2 and len(string1) == len(string2):
        c1 = build_counts(string1)
        c2 = build_counts(string2)
        return c1 == c2
    else:
        return False

print(anagram("rac", "car"))