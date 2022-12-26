#######################################################
# Part I: Given the code below, read and understand what is happening.
# 1. There is a bug in this code, run the tests to find the bug and fix it
# 2. Add an additional test for the list_contacts method
#######################################################
from typing import Union

class PhoneBook:

    def __init__(self):
        self.records = {}
    
    def set_phone_number(self, name: str, phone_number: str):
        self.records[name] = phone_number

    def get_phone_number(self, name: str) -> Union[str, None]:
        return self.records.get(name)

    def list_contacts(self):
        return sorted(self.records.keys())


pb = PhoneBook()
pb.set_phone_number('Foo', '123-456-7890')
pb.set_phone_number('Bar', '234-567-8901')
pb.set_phone_number('Baz', '345-678-9012')

assert pb.get_phone_number('Foo') == '123-456-7890'
assert pb.get_phone_number('Bar') == '234-567-8901'
assert pb.get_phone_number('Bob') is None
assert pb.list_contacts() == ['Bar', 'Baz', 'Foo']
# TODO: Add test for list_contacts method











# def intersection_of_2_lists(list1, list2):
#       print(set(list1).intersection(list2))

# l1 = [1,2,3,6,3,2]
# l2 = [3,2,1,2,3]

# intersection_of_2_lists(l1,l2)

# def intersection_of_2_lists_v2(l1, l2):
#   l1 = set(l1)
#   print([ num for num in l1 if num in l2])

# intersection_of_2_lists_v2(l1, l2)


# l1 = [1,3,4,6,7]
# l2 = [1,1,4,5]

# def inter_of_2_sorted(l1, l2):
#   l1_cntr = 0
#   l2_cntr = 0
#   intersection = []
#   while l1_cntr < len(l1) and l2_cntr < len(l2):
#     if l1[l1_cntr] > l1[l1_cntr - 1]:
#       if l1[l1_cntr] == l2[l2_cntr]:
#         intersection.append(l1[l1_cntr])
#         l2_cntr += 1
#     if l2[l2]




#inter_of_2_sorted(l1,l2)
    # 




