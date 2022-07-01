# Write a recursive function is_palindrome that accepts a string text as a parameter. It returns a boolean value indicating whether or not that string is a palindrome  .

# Input text	Return value
# "racecar"	True
# "raecar"	False

def is_palindrome(text):
    if len(text) == 0:
        return True
    elif text[:1] != text[-1:] :
        return False
    else:
        return is_palindrome(text[1:-1])

        

def test_is_palindrome_success():
    assert is_palindrome("racecar")


def test_is_palindrome_not_palindrome():
    assert not is_palindrome("raecar")