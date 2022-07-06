# Given a sentence, return a new string that removes all blanks in a sentence. 
# Don't forget your edge cases!

# Example Input: " In     Th    eNo  tToo   Dist  an   tFu   tu  re"
# Example Output: "InTheNotTooDistantFuture"

# Example Input: " "
# Example Output: " "

sentence = " In     Th    eNo  tToo   Dist  an   tFu   tu  re"
d = sentence.split()
"".join(d)





# Given a sentence, return a new string that turns the sentence into an acronym. 
# Don't forget your edge cases!


# Example Input: "Somewhere in time and space"
# Example Output: "SITAS"

# Example Input: "Hot blooded, check it and see"
# Example Output: "HBCIAS"

sentence1 = "Somewhere in time and space"
d1 = sentence1.split()
first = ""
for i in range(len(d1)):
    first += d1[i][0]
print(first.upper())


# Given a string, return an integer value of the numeric characters from the string. 
# Don't forget your edge cases!

# Example Input: "0?3af4([4m5HW7"
# Example Output: 34457

# Example Input: "abdfg[Bwk!f?"
# Example Output: None

s = "0?3af4([4m5HW7"
# s_split1 = int(filter(str.isdigit, s))
s_split = list(s)
print(s_split)
numbers = []
for i in s_split:
    if i.isnumeric():
        numbers.append(i)
print(int("".join(numbers)))