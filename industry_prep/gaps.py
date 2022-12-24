'''
Your goal is to write a function that finds gaps between given intervals.

The intervals will be an UNSORTED tuple containing tuples. 
Each inner tuple will represent an integer interval. 
It will have two elements: the first element is the beginning of the interval, 
the second element is the end of the interval. 
The first element is guaranteed to be strictly less than the second element.

Here is an example of an input tuple:

intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)

For clarity of the example, this tuple is sorted. However, 
note that some of the other test cases are NOT SORTED.

In this example, we can see that the earliest interval ends at 10, 
and the next interval starts at 12. Thus, there is a gap from 10 to 12. 
Similarly, we can see there are two other gaps. 
Below is a tuple (in sorted order) showing all of the gaps for this example:

expected_output = (
    (10, 12), 
    (15, 16), 
    (25, 27)
)

Note that there is NOT a gap at 20. One interval ends at 20, and another starts at 20. Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals.

Write a function that accepts the UNSORTED input intervals and returns a SORTED tuple of tuples containing all the gaps.
'''

def find_gaps(intervals):
    # copy and sort the intervals
    # The default sorting behavior sorts by the first element in the tuple
    # note that intervals.sort() DOES NOT WORK (tuples are immutable)
    intervals = sorted(intervals)

    # will hold the gaps as they are found
    # to be converted to tuple at the end
    gaps = []
    
    # loop over each interval, comparing it to the next one
    # do not include the last interval because there is not a next one after it
    for i in range(len(intervals) - 1):
        current  = intervals[i]
        next = intervals[i+1]
        
        # if the end of the current interval is smaller than the 
        # start of the next one there is a gap that must be added
        if current[1] < next[0]:
            gaps.append((current[1], next[0]))

    # convert to tuple to match expected output types
    return tuple(gaps)

intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
assert find_gaps(intervals_1) == ((10, 12), (15, 16), (25, 27))

intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)
assert find_gaps(intervals_2) == ((10, 12), (15, 16), (25, 27))

intervals_3 = (
    (17, 35),
)
assert find_gaps(intervals_3) == tuple()

intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)
assert find_gaps(intervals_4) == tuple()


print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if there is invalid input?
A: You can assume the input will be valid.

Q: What should I do if the input is an empty tuple?
A: You can assume there will be at least one interval present in the input.

Q: Do I have to worry about non-integers? (floats, complex, etc?)
A: You can assume the intervals will always be integers

Q: What should I do if there are no gaps?
A: Return an empty tuple (see last two test cases)

Q: What should I do if intervals overlap?
A: Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals. For example, there would NOT be intervals of (15, 21) and (20, 30)

Q: Will the input have a single interval with the same start and end? For example, (20, 20)
A: No.

Q: Can my output have a single interval with the same start and end? For example, (20, 20)
A: Also no.

Q: Does my output need to be sorted?
A: Yes.

Q: Is the input guaranteed to be sorted?
A: No.

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

 - If they're struggling to sort the input tuple for more than a few minutes, suggest that they work on the rest of the problem and come back to sorting the input if they have time at the end. The first test case is already sorted, so they'll be able to test the rest of their logic.

- If they finish everything else and are still stuck on sorting the input, encourage search for how to sort a tuple in Python. If they're still stuck, you can just tell them to use 'sorted'.

- If your candidate is returning a list and doesn't recognize why their code is not passing them the tests, ask them what the expected output types are.

- If your candidate struggles to make an empty tuple, you can tell them to use 'tuple()'. If they struggle to make a tuple with a single element, you can tell them to use '(some_data,)'. Note the comma.

- If your candidate struggles to work with the outer tuple when constructing their gaps, you can encourage them to have the outer data structure to be a list to start and convert it to a tuple at the end (like the above example does).

 -------------------------------------------------
"""
