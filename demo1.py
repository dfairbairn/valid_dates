"""
DEMO 1:
This file demonstrates the basics of opening, reading, writing, and closing a file
"""

# Demo 1
f = open('example.csv','r')
mystring = f.readline()  # Comment: mystring now contains "amazon_movie_rental,date_watchable\n"'
print("String I just read: '" + mystring + "'")
f.close()

# You'll notice how readline() also grabbed the newline character, which can look annoying when we resave it!
# Let's trim mystring down so it includes all but its last character
mystring = mystring[:-1]
# read this as "[everything (:) in the mystring array up to the 1st to last character (-1)]"


# Even if the file is closed, I still have 'mystring' filled with data, lets put in an output file
f_out = open('output.txt', 'w')
f_out.write(mystring)
f_out.close()
print("Just wrote '" + mystring + "' to a file!")
