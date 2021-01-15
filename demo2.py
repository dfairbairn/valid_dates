"""
This file shows how you can use the CSV module to loop through a CSV file with 2 columns
"""

import csv

# Demo 2: use the python csv module to read each line/data entry in the CSV data
f = open('example.csv','r')
# Build a 'csv reader' object using our filehandle
example_reader_object = csv.reader(f, delimiter=',')

# The example_reader_object is meant to be used in a loop like so:
for csvrow in example_reader_object:
    print("\nThe next row when converting to string is: " + str(csvrow))

    # The two data fields in the row can be separated easily like so though:
    movie_id, movie_rental_date = csvrow
    print("Movie ID: " + movie_id)
    print("Movie Rental Date: " + str(movie_rental_date))

f.close()

