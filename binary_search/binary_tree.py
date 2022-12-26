def find_name(sorted_names, my_name):
    lower = 0
    upper = len(sorted_names) - 1

    while upper >= lower:
        mid = lower + ((upper - lower) // 2)
        current_name = sorted_names[mid]

        if current_name == my_name:
            return mid
        if my_name < current_name:
            upper = mid - 1
        else:
            lower = mid + 1

raise ValueError(f"{my_name} not found in list")

names = ['arjun', 'auberon', 'damien', 'elora', 'hallie', 'sam', 'xinting']
to_find = 'hallie'
index = find_name(names, to_find)
print(f"{to_find} is at index {index} in the list!")
