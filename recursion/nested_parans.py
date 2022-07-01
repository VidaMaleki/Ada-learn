# Write a function is_nested_parens that accepts a string parens of only parentheses. It returns True if those parentheses are properly nested, and False if they are not. You may assume that no non-parenthesis characters will be passed to this function.

# Example parens	Expected Output
# "((()))"	True
# ""	    True
# "(())))"	False

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])
        
        
# def is_nested_parens(parens):
#     if parens == "":
#         return True
#     if len(parens) % 2 != 0:
#         return False
#     if parens[0] == "(" and parens[-1] == ")":
#         new_string = parens[1:-1]
#     else:
#         return False
#     return is_nested_parens(new_string)


def test_is_nested_parens():
    parens = "((()))"

    assert is_nested_parens(parens)


def test_is_nested_parens_empty_str():
    assert is_nested_parens("")


def test_is_nested_parens_not_matching_length():
    parens = "(())))"

    assert not is_nested_parens(parens)