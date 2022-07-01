"""
You will be given a data structure containing information on different recpies. It will be a list of tuples, where each tuple represents a single recipe. The tuple will have three elements in this order: the name of the recipe, the name of the chef who created it, and a tuple of ingredients.

For example:

[
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]

We are interested in which chefs use the greatest variety of ingedients across all of their recipes. For example, Xinting uses the following ingredients (in alphabetical order):

['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']

This is a larger number of ingredients than any other chef uses. Thus, we will say that Xinting is the most varied chef.

Write a function that takes in a recipes data structure and returns the top two most varied chefs, along with an alphabetically sorted list of the ingredients they each use. This output must be a list of tuples. Each tuple will have two elements in this order: the name of the chef, and a sorted list of the unique ingredients they use.

Examples:
recipes_1 = [
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
most_varied(recipes_1) => [
  ('Xinting', ['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']), 
  ('Amy', ['Cheese', 'Chicken Cream', 'Pepper', 'Tater tots'])
]

recipes_2 = [
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
most_varied(recipes_2) => [('Sam', ['Beef', 'Cheese', 'Tortilla']), ('Hallie', ['Oil', 'Potato'])]
"""

def most_varied(recipes):
  # Create a dictionary of chefs to a set of ingredients they use
  # For example {"Sam": {"Tortilla", "Beef", "Cheese"}}
  unique_ingredients = {}
  #Iterate over the recipes, unpacking the needed values
  for _, chef, ingredients in recipes:
    # If this is the first time we have seen this chef
    if chef not in unique_ingredients:
      # Start with all the ingredients for the first recipe
      unique_ingredients[chef] = set(ingredients)
    else:
      # Add each ingredient from the new recipe
      # The set avoids creating duplicates
      for ingredient in ingredients:
        unique_ingredients[chef].add(ingredient)
  
  # Create a list of tuples. where each tuple contains
  # the number of unique ingredients used, then the chef
  # For example: [(2, "Hallie"), (3, "Sam")]
  counts = []
  for chef, ingredients in unique_ingredients.items():
    counts.append((len(ingredients), chef))

  # Sort the counts in descending order and select the top 2
  counts.sort(reverse=True)
  top_two = counts[:2]

  # Convert the data into the final result
  result = []
  for _, chef in top_two:
    sorted_ingredients = sorted(list(unique_ingredients[chef]))
    result.append((chef, sorted_ingredients))

  return result
  
recipes_1 = [
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
assert most_varied(recipes_1) == [
  ('Xinting', ['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']), 
  ('Amy', ['Cheese', 'Chicken Cream', 'Pepper', 'Tater tots'])
]

recipes_2 = [
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
  ('Sam', ['Beef', 'Cheese', 'Tortilla']),
  ('Hallie', ['Oil', 'Potato'])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")

"""
NOTES FOR INTERVIEWER

--------- Clarifying questions ---------------

Q: How should I handle invalid input?
A: You can assume the input will be valid.

Q: How should I handle empty input? Or input with only one chef?
A: You can assume the input will be non-empty and have at least two chefs.

Q: Does capitalization matter?
A: Yes.

--------- Hints -------------------------------

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.

- If your candidate is struggling with a subpart of the problem (e.g. sorting or getting the top 2), encourage them to first focus on writing a solution to a simpler version of the problem that does not include those requirements.

- If your candidate is struggling to get unique elements, ask them what data structure (sets) could help them there.

"""