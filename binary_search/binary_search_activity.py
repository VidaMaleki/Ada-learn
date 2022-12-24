"""
Your goal is to write a function that returns the name of a student with a given ID number.

The information about the students will be a list of tuples. Each tuple will represent a single student. The first element in the tuple will be the student's name. The second element will be the student's ID number. For example:

sorted_students = [
    ('damien', 7),
    ('sam', 10),
    ('auberon', 23),
    ('hallie', 31),
    ('xinting', 42),
    ('arjun', 88),
    ('elora', 92)
]

You are guaranteed that the list is sorted by ascending ID number (NOT sorted alphabetically). You are also guaranteed each ID number is unique.

Write a function that accepts a sorted list of student tuples and the ID number of a student we're interested in. It should return the name of the student with that ID number.

For example:
find_student(sorted_students, 23) # Should return 'auberon'

If no student has the specified ID number, your function should return None.

YOUR SOLUTION MUST HAVE A LOGARITHMIC TIME COMPLEXITY AND A CONSTANT SPACE COMPLEXITY.
"""

def find_student(sorted_students, student_id):
    low = 0
    high = len(sorted_students) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if sorted_students[mid][1] < student_id:
            low = mid + 1
        # If x is smaller, ignore right half
        elif sorted_students[mid][1] > student_id:
            high = mid - 1
        # means x is present at mid
        else:
            return sorted_students[mid][0]
 
    # If we reach here, then the element was not present
    return None


sorted_students = [
    ('damien', 7),
    ('sam', 10),
    ('auberon', 23),
    ('hallie', 31),
    ('xinting', 42),
    ('arjun', 88),
    ('elora', 92)
]
assert find_student(sorted_students, 23) == "auberon"
assert find_student(sorted_students, 88) == "arjun"
assert find_student(sorted_students, 7) == "damien"
assert find_student(sorted_students, 92) == "elora"
assert find_student(sorted_students, 33) is None
print("All tests passed!")