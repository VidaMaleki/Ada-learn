#*************** Append ****************

# The append() method appends an element to the end of the list.
# syntax >>>  list.append(elmnt)     Big O >>> O(1)
# add string to a list

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# output  >>> ['apple', 'banana', 'cherry', 'orange']


#*************** Extend ****************

#The extend() method adds the specified list elements (or any iterable) to the end of the current list.

#syntax  >>> list.extend(iterable)       Big O >>> O(K)

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

#output >>> ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']


#*************** Insert ****************

#The insert() method inserts the specified value at the specified position.
# syntax >>>  list.insert(index, elmnt)    Big O >>> O(n)

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

#output  >>>  ['apple', 'orange', 'banana', 'cherry']

#*************** clear ****************
#The clear() method removes all the elements from a list.
# syntax >>> list.clear()    Big O >>> O(?)

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

#output  >>>  2

#*************** Count ****************
#The count() method returns the number of elements with the specified value.
# syntax >>> list.count(value)    Big O >>> O(?)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
#output  >>>  2

#*************** Index ****************
#The index() method returns the position at the first occurrence of the specified value.
# syntax >>> list.index(elmnt) Big O >>> O(?)

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

#output  >>>  2

#*************** pop ****************
#The pop() method removes the element at the specified position.
# syntax >>> list.pop(i)   last character -> Big O >>> O(1)  ||  with index-> Big O >>> O(n)
# Note: The pop() method returns removed value.
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

#output  >>>  'banana'

#*************** remove ****************
#The remove() method removes the first occurrence of the element with the specified value.
# syntax >>> list.remove(elmnt)    Big O >>> O(n)
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

#output  >>>  ['apple', 'cherry']

#*************** reverse ****************
#The reverse() method reverses the sorting order of the elements.
# syntax >>> list.reverse()   Big O >>> O(n)

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

#output  >>>  ['cherry','banana', 'apple']

#*************** sort ****************
#The sort() method sorts the list ascending by default.
#You can also make a function to decide the sorting criteria(s).
# syntax >>> list.sort(reverse=True|False, key=myFunc)      Big O >>> O(n log n)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

# A function that returns the 'year' value:
def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
# [
    # {'car': 'Mitsubishi', 'year': 2000}, 
    # {'car': 'Ford', 'year': 2005}, 
    # {'car': 'VW', 'year': 2011}, 
    # {'car': 'BMW', 'year': 2019}]

# A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

# output >>> ['Mitsubishi', 'Ford'', 'BMW', 'VW']