# Given a number and another number that represents a digit's place,
#  create a function that isolates the value of the number at a specific place and returns it.
# 0 represents the ones place, 1 represents tens place, 2 represents the hundreds place, etc.

# Example Input: 44154, 2
# Example Output: 1
# Example Input: 251, 5
# Example Output: None

# Extra Challenge: Work with decimals next.
# Example Input: 54.06, -2
# Example Output: 6

def find_index(num, x):
    
    num = list(str(num))
    if x < 0:
        x = -(x)
        for i in range(len(num)):
            if num[i] == ".":
                return num[i + x]
    else:
        return num[x]


find_index(54.0623, -4)


def return_single_digit(num, place):
    if place ==0:
        return num % 10
    
    divide_by = 10
    for i in range(1, place):
        divide_by *= 10
        
    return (num// divide_by) % 10

return_single_digit(44154, 2)


# GPC is the robot responsible for running her team's spaceship. 
# She needs a way to log her every movement on the ship, 
# so that her teammates can find her using a few simple computer functions.

# Starting at homebase [0,0] every morning,
# she logs her movements by increasing/decreasing her x and y coordinates by calling the function move_by(x,y)
# Every night before she powers off, she resets her location coordinates to [0,0] with the function reset()
# If a teammate wants to find her, they can use the functions y_location() and x_location() to find her current x and y coordinates
# Some of her teammates complain that calling two functions is a pain.
# How could GPC use these two functions to create a more user-friendly readout?

# Homebase is [0,0]

# move_by(-2,4)
# move_by(0,2)
# y_location()
# ⇒ 6
# x_location()
# ⇒ -2
# move_by(4,6)
# x_location()
# ⇒ 2
# reset()

COORDS = [0,0]
def move_by(x, y):
    COORDS[0] += x
    COORDS[1] += y
    
def reset():
    COORDS[0] = 0
    COORDS[1] = 0
    
def x_location():
    return COORDS[0]

def y_location():
    return COORDS[1]

def display():
    return f'GPC is currently at coordinates {COORDS[0]}, {COORDS[1]}'
move_by(2, 4)
move_by(4, 6)
move_by(1, 8)
print(display())



