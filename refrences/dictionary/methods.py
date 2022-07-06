#*************************  get() ***************************
#The get() method returns the value of the item with the specified key.

#syntax  >>> dictionary.get(keyname, value)
#keyname	Required. The keyname of the item you want to return the value from
#value	Optional. A value to return if the specified key does not exist.
#Default value None    

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("price", 15000)

print(x)
# output >>> 15000

#*************************  fromkeys() ***************************
#The fromkeys() method returns a dictionary with the specified keys and the specified value.

#syntax  >>> dict.fromkeys(keys, value)
#value	Optional. The value for all keys. Default value is None

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x, 0)

print(thisdict)
#output >>>   {'key1': 0, 'key2': 0, 'key3': 0}

#*************************  items() ***************************
#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

# The view object will reflect any changes done to the dictionary, see example below.
# syntax >>> dictionary.items()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)
# output >>> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])