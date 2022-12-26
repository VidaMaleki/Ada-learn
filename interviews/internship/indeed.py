# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



def max_product(nums):
    high = []
    positives = []
    negatives = []
    high_negatives = []
    high_positives = []
    
    for number in nums:
        if number < 0:
            negatives.append(number)
        elif number > 0: 
            positives.append(number)

    for i in range(3):
        high_negatives.append(min(negatives))
        high_positives.append(max(positives))
        high_negatives.remove(min(negatives))
        high_positives.remove(max(positives))
                              
    if high_negatives[0] * high_negatives[1] > high_positives[1] * high_positives[2]:
        return high_negatives[0] * high_negatives[1] * high_positives[0]
    else:
        return high_positives[0] * high_positives[1] * high_positives[2]

    


print(max_product([-9,-8,-1,2,3,4]))