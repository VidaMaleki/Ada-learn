"""
A potato is a plant that has multiple parts, such as leaves, berries, and tubers (the tubers are the actual starchy root vegetables that grow underground).

Our goal will be to create classes that model a potato plant and its tubers.

### WAVE 1 ###

Provided for you is a Plant class. This Plant class should NOT be modified. Instead, you should make a new class, Potato that is a subclass of Plant.

Each potato should have two instance variables, 'energy' and 'tubers'. 'energy' should be a number that represents how much energy the potato plant itself currently has. 'tubers' should be a list containing the tubers the potato plant has.

The Potato's constructor should take a starting energy and set its own energy to that starting energy. The potato should start off with no tubers.

### WAVE 2 ###

You should create a class, Tuber. It should have an instance variable 'energy' which is a number that represents how much energy the tuber has. A Tuber begins with 30 energy.

You should add an instance method to Potato, 'sprout_tuber'. It should create a new tuber and add it to that potato's list of tubers. It should also decrease the potato plant's energy by 30.

If the potato has less than 30 energy, no action should be taken when this function is called.

### WAVE 3 ###

In the Potato class you should override the 'absorb_sunlight' method. It should accept the same arguments as before. However, if the potato plant has tubers, it should distribute the new sunlight_energy as follows:

  - The potato plant itself recieves half of the sunlight_energy.
  - The remaining sunlight_energy is split evenly between the potato's tubers.

If the potato plant has no tubers, the plant recieves all the energy.
"""

# DO NOT MODIFY THE PLANT CLASS
class Plant:
    def __init__(self, starting_energy):
        self.energy = starting_energy

    def absorb_sunlight(self, sunlight_energy):
        self.energy += sunlight_energy

    def __str__(self):
        return f'I am a {type(self).__name__} and I have {self.energy} energy!' 


class Potato(Plant):
    def __init__(self, starting_energy):
        super().__init__(starting_energy)
        self.tubers = []

    def sprout_tuber(self):
        if self.energy > 30:
            self.tubers.append(Tuber())
            self.energy -= 30

    def absorb_sunlight(self, sunlight_energy):
        self.energy += sunlight_energy
        if len(self.tubers) > 0:
            energy_for_tuber = sunlight_energy // (len(self.tubers) * 2)
            for tuber in self.tubers:
                tuber.energy += energy_for_tuber
                self.energy -= energy_for_tuber


class Tuber:
    def __init__(self):
        self.energy = 30



########## WAVE 1 ##########
# Checking the behavior for creating an instance of Potato
assert issubclass(Potato, Plant), "Potato must be a subclass of Plant"
my_potato = Potato(70)
assert my_potato.energy == 70
assert my_potato.tubers == []
assert str(my_potato) == 'I am a Potato and I have 70 energy!'
print("Wave 1 passed!")


########## WAVE 2 ##########
# Checking the behavior for sprouting one tuber
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 1
first_tuber = my_potato.tubers[0]
assert isinstance(first_tuber, Tuber), "A Potato's tubers must be instances of class Tuber"
assert first_tuber.energy == 30
assert my_potato.energy == 40

# Checking the behavior for sprouting a second tuber
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 2
assert my_potato.tubers[0].energy == 30
assert my_potato.tubers[1].energy == 30
assert my_potato.energy == 10

# Checking the behavior for attempting to sprout a tuber when the potato
# does not have enough energy
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 2
assert my_potato.tubers[0].energy == 30
assert my_potato.tubers[1].energy == 30
assert my_potato.energy == 10
print("Wave 2 passed!")


########## WAVE 3 ##########
# Checking the behavior for absorbing sunlight for a 
# potato with multiple tubers
my_potato.absorb_sunlight(100)
assert my_potato.energy == 60
assert my_potato.tubers[0].energy == 55
assert my_potato.tubers[1].energy == 55

# Checking the behavior for absorbing sunlight for a 
# potato with one tuber
new_potato = Potato(30)
new_potato.absorb_sunlight(40)
assert new_potato.energy == 70
print("Wave 3 passed!")

print("All tests passed! If time remains, discuss alternate design decisions you could have made, or other ways you may think to add more functionality to your code.")

"""
--------- Delivery Notes ---------------------

THIS QUESTION IS MEANT TO BE DONE ONE WAVE AT A TIME!

- Please only explain the first wave to your interviewee first. Do not discuss the second wave or have them begin implementation on it until they have the first wave fully working. Progress in this fashion for each wave.

THE TESTS ARE HELPFUL!

- Encourage your interviewee to closely look at the tests before they begin implementation.

--------- Clarifying Questions ---------------

Q: How should I handle invalid input? 
A: You can assume the input will be valid.

Q: Can I modify the Plant class?
A: No.

Q: Shold the energies be ints or floats?
A: Either should work for the given test cases.

Q: Where can I learn more about potatoes?
A: "The History and Social Influence of the Potato" by Dr. Redcliffe N. Salaman.

--------- Hints -------------------------------

- Make sure your candidate's classes aren't accidentally indented and inside the Plant class! The auto-indenting Replit does makes it easy to make this mistake. If you see your candidate do this, you can immediately let them know.

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.

"""