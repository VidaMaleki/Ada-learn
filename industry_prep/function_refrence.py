'''
WAVE 1: Implementing min_with_ties

It will take in two arguments, a list and a scorer function.
It should return a list containing the elements that are tied for the lowest score.
Elements in the returned list should be in the order the appeared in the original list.

Example:
sentence = ["how", "are", "you", "today"]
min_with_ties(sentence, len) -> ["how", "are", "you"]
'''

def min_with_ties(data, scorer):
    pass

# Tests
sentence = ["how", "are", "you", "today"]
assert min_with_ties(sentence, len) == ["how", "are", "you"]
numbers = ["1", "55", "4", "1"]
assert min_with_ties(numbers, int) == ["1", "1"]


'''
WAVE 2: Using min_with_ties

Write an additional function and class to pass into min_with_ties.

1. Create an Item class that has an attribute 'condition'
2. Write a function that takes an item as an argument and returns its condition.
2. Create a list of different Items with different conditions
3. Write asserts that call min_with_ties with the list you created and get_item_condition
4. Write asserts that use a lambda function instead of get_item_condition to achieve the same result
'''

class Item:
    # Implement class here!
    pass


def get_item_condition(item):
    # Write a scoring function here!
    pass

# Write asserts here!


'''
WAVE 3: Using min_with_ties creatively

Come up with a new function and dataset to pass to min_with_ties. It can be anything you want! Get creative! Test it out with some asserts.
'''

# Get creative here!

'''
WAVE 4: Implementing median

It will take in two arguments, a list and a scorer function.
It should sort the items based on their score, and return the item that is exactly in the middle.

Make more tests further test this!

HINT: The 'sorted' function has an optional parameter named 'key'. Look up what that argument does!

Example:
words = ["hello", "a", "the", "to", "with"]
median(words, len) -> "the"
'''

def median(data, scorer):
    pass

# Uncomment this test when ready!
# words = ["hello", "a", "to", "the", "with"]
# assert median(words, len) == "the"