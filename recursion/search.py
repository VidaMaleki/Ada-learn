# Write a function search that accepts an unsorted array of integers, array, and an integer value to find, query. It returns True if query is found in array, and False otherwise. Make the algorithm recursive.

# Be sure to implement search using recursion.

# Here are the tests:


def search(array, query):
    if not array :
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)
    


def test_search_success_unsorted():
    assert search(["b", "c", "a"], "a")


def test_search_empty_array():
    assert not search([], "a")


def test_search_success_first_item():
    assert search(["a", "b", "c"], "a")


def test_search_not_found():
    assert not search(["a", "b", "c"], "🌈")