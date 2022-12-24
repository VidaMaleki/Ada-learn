"""
Create a function that takes a string consisting of one or more all-lowercase words separated by spaces. 
It should return a new string converted to "pig Latin," 
where each word has its first letter moved to the back and 
the letters "ay" are added to the end of the word. However, 
words starting with a vowel (a, e, i, o, or u) should not be altered.

Examples:

pig_latin("something") # should return "omethingsay"
pig_latin("awesome") # should return "awesome" (words starting with a vowel should not be altered)
pig_latin("latin is a hard language") # should return "atinlay is a ardhay anguagelay"
pig_latin("y") # should return "yay"
pig_latin("e") # should return "e"
"""
def pig_latin(sentence):
    vowel = ('a', 'e', 'i', 'o', 'u')
    splited = sentence.split()
    print(splited)
    
    if splited[0] in vowel:
        splited= splited[0][1:]+ splited[0] + 'ay'
    print(splited)
    return "".join(splited)





# def pig_latin(sentence):
#   # split the sentence into a list of words
#   words = sentence.split()

#   # for each new word, use the helper to convert the word
#   # into pig latin. Put those words into new_words
#   new_words = []
#   for word in words:
#     new_words.append(pig_latin_single_word(word))

#   # Join all the words together with spaces to make the final string
#   return " ".join(new_words)

# # Helper that converts a single word to pig latin
# def pig_latin_single_word(word):
#   # if the first letter is a vowel, don't change anything
#   if word[0] in 'aeiou':
#     return word

#   # otherwise, if it's a consonant
#   # start with all but the first letter of the word
#   new_word = word[1:]
#   # add the first letter to the end of the word
#   new_word += word[0]
#   # add the suffix
#   new_word += "ay"
#   return new_word


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if the input is not a string? Or if the string is empty?
A: You do not need to worry about this case. You can assume the input will be a string with at least one letter in it.

Q: How should I handle capital letters?
A: You can assume the input will not have any capital letters.

Q: What should I do with punctuation, numbers, etc.?
A: You can assume the input will include only letters and spaces.

Q: What should I do if there's extra spaces?
A: You can assume there will be exactly one space in between words and no extra spaces at the beginning or end of the string.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

 - If they're having trouble determining how to handle multiple words, encourage them to first write code to solve the case where there's only a single word in the string

 - If they're having trouble determining how to check if a word starts with a vowel, encourage them to ignore the vowel condition at first, and alter all words.

 - If your candidate is struggling to convert a single word, ask them to do it step by step. Ask them:
   - How do you get the first letter of a string?
   - How do you remove the first letter from a string?
   - How do you add letters to the end of a string?

 -------------------------------------------------

"""