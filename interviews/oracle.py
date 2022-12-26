# write a function that return true or flase.
# if a word is palindrome
# split the string
# loop through the left hand of the string 
#  compare that to right handside 
# if all of the letters present and in order return true, else return false.
# string[::-1]
# def palindrome(string):
#   reverse = string[::-1]

#   if string == reverse:
#     return True
#   else:
#     return False


# # string = "tacocat"
# string = "kayla"


# print (palindrome(string))


def sentence (string):

    # only_words = ""

    only_words = string.split()

    print (only_words)

    counter = 0

    for word in only_words:
        counter += 1