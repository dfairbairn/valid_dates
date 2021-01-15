"""
This file shows how to create a dictionary object with strings as keys and strings as data for those keys
"""

# Demo 3: Create a dictionary with things in it
my_dict = {}
print("My empty dictionary: ")
print(my_dict)

my_dict['movie_ID_1'] = "Tenet"
my_dict['movie_ID_2'] = "Rapunzel"
# Now the dictionary should look like it has a couple entries in it
print("My fuller dictionary: ")
print(my_dict)

# What keys are in our dictionary right now?
print("Dict keys: ")
print(my_dict.keys())

# What values are in our dictionary right now, totally ignoring which key they're assigned to?
print("Dict values: ")
print(my_dict.values())
