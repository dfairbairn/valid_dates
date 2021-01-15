"""
This file demonstrates how to create a dictionary where its keys each map to a full list
"""

# Demo 4: Creating a dictionary where each 'key' maps to a list that we add to
keys_in_dict = ['worf', 'geordie', 'beverly']
qualities_dict = {}
print("My empty dictionary: ")
print(qualities_dict)

# First set up the dictionary so that it *knows* its supposed to have the keys above, and each should translate to an empty list
for key in keys_in_dict:
    qualities_dict[key] = []
print("My initialized dictionary that doesnt have data inputted yet: ")
print(qualities_dict)

# Now lets enter the qualities for somebody:
print("Worf's qualities initially: " + str(qualities_dict['worf']))
qualities_dict['worf'].append("honour-driven")
qualities_dict['worf'].append("vigilant")
qualities_dict['worf'].append("most improved character from TNG to DSN?")
print("Worf's qualities: " + str(qualities_dict['worf']))
qualities_dict['geordie'].append("unlucky with ladies")
qualities_dict['geordie'].append("brilliant engineer")
qualities_dict['beverly'].append("elegantly intelligent")
print("The dictionary of lists after filling: ")
print(qualities_dict)
