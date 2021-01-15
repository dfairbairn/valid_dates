"""
This file houses the proof of concept code in script format
"""
import csv

movie_dict = {}

def is_date_valid(keyid, date, lookup_dict=movie_dict):
    """
    Function to see if a date is valid for a given key.
    :param keyid: key into the dictionary
    :param date: a date to check for in the list corresponding to 'keyid'
    :param lookup_dict: lookup dictionary
    Note, the date is treated as an exact date string
    """
    if keyid not in movie_dict.keys() or type(movie_dict[keyid]) != list:
        return False
    return date in movie_dict[keyid]

# 1. Open file
f = open('example.csv','r')
reader = csv.reader(f)

# 2. Initialize the dictionary
# a. Skip the first line of the file because its got column names
reader.__next__()

# b. Learn all the IDs in the first column
for movie_id, movie_rental_date in reader:
    if movie_id not in movie_dict.keys():
        movie_dict[movie_id] = []
# c. Return reader to the beginning of the file
f.seek(0)           # Tell the file handle to seek the 0th position of the file
reader.__next__()   # Bump past the first line again

# 3.
for movie_id, movie_rental_date in reader:
    # This time we know all the movie_id values are in the movie_dict
    if movie_rental_date not in movie_dict[movie_id]:
        movie_dict[movie_id].append(movie_rental_date)

print("Final lookup dictionary with ID keys and unique Date entries for each key: ")
print(movie_dict)

print("Attempting to lookup '2020-10-03' for 'Tenet' in the dictionary...")
print("is_date_valid('Tenet', '2020-10-03'): " + str(is_date_valid('Tenet', '2020-10-03', movie_dict)))
f.close()

