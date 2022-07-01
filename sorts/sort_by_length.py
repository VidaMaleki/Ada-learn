# There's no better way to get familiar with sorting algorithms than to implement one yourself!

# Without using Python's sort() method (or anything like that), implement sort_by_length based on insertion sort.

# sort_by_length is a function that takes in one string. It returns a list of strings, where the items are the words from the string, ordered by length. Words with shorter length are placed before words with longer length.

# When words are tied for length, maintain the order they appeared in the original string.

# Here are the tests:

def sort_by_length(sentence):
    sentences = split(sentence)
    smallest = sentences[0]
    
    for i in range(len(sentence)):
        if len(sentence[i]) < len(smallest):
            sentece.insert(sentence[i])
            smallest = sentence[i]
        else:
            


def test_sort_by_length_with_empty_string():
    assert sort_by_length("") == []


def test_sort_by_length():
    assert sort_by_length("I love great awesome words") == [
        "I", "love", "great", "words", "awesome"]


def test_sort_by_length_checks_smallest_word_last():
    assert sort_by_length("love great awesome words I") == [
        "I", "love", "great", "words", "awesome"]


def test_sort_by_length_equal_length_maintains_order():
    assert sort_by_length("words of equal length") == [
        "of", "words", "equal", "length"]