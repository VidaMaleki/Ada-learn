# Given a string with capital letters, punctuation and spaces, determine if the sequence is a palindrome. Return true or false. Don't forget your edge cases!


# Example Input: "bl o lb"
# Example Output: True

# Example Input: "Hey ,sis, yeh"
# Example Output: False

# Example Input: "RacecaR"
# Example Output: True

# Do not store a new copy of the string. Try to do this with O(1) space complexity

word = "Hey ,sis, yeh"

def palindrom(word):
    return  word == word[::-1]
        


print(palindrom(word))


# Given a string with capital letters, punctuation and spaces, return the longest palindrome sequence. 
#Don't forget your edge cases!


# Example Input: "Hey ,sis, yeh"
# Example Output: "ey, sis, ye"

# Example Input: "racecars are great!"
# Example Output: "racecar"

# Example Input: "summer love"
# Example Output: "mm"
word = "racecars are great!"

def word_chacker(word):
    split_word = list(word)
    j = -1
    for i, num in enumerate(split_word):
        if split_word[i] != split_word[j]:
            split_word.remove(split_word[i])
            split_word.remove(split_word[j])
        j -= 1
    return "".join(split_word)


def chek_longest(word):
    splited_s = word.split()
    print(splited_s)
    s = []
    for w in splited_s:
        b = word_chacker(w)
        s.append(b)
        print(b)
    print(s)
    return s


print(chek_longest(word))


def longestPalindrome(s):
    # Create a string to store our resultant palindrome
    palindrome = ''

    # loop through the input string
    for i in range(len(s)):

        # loop backwards through the input string
        for j in range(len(s), i, -1):

            # Break if out of range
            if len(palindrome) >= j-i:
                break

            # Update variable if matches
            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break

    return palindrome

