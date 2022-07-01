# Write a function reverse that accepts a string text as a parameter. It returns the reverse of text by reversing all characters in the string.

# Here are the tests:

def reverse(text):
    if text == "":
        return text
    else:
        return reverse(text[1:]) + text[0]
        
# def reverse(word):
#     if len(word) == 0:
#         return ""

#     return word[len(word)-1] + reverse(word.rstrip(word[len(word)-1]))





def test_reverse_word():
    assert reverse("cat") == "tac"


def test_reverse_single_character():
    assert reverse("a") == "a"


def test_reverse_empty_string():
    assert reverse("") == ""