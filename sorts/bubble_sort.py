

def bubble_sort(array):
    i = 0
    # Begin the outer loop
    while i < len(array) - 1:
        j = 0
        # Begin the inner loop
        while j < (len(array) - i - 1):
            # Compare two adjacent items
            if array[j] > array[j+1]:
                # Swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            j += 1
        i += 1