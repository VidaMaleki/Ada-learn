"""
Your goal is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Name the function array_diff.
"""
arr1 = [1,2,2,2,3]
arr2 = [2]
def array_diff(arr1, arr2):
    d = []
    for num in arr1:
        if num not in arr2:
            d.append(num)
    return d
    # return list(set(arr1) - set(arr2))

print(array_diff(arr1, arr2))