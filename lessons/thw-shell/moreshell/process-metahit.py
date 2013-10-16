#!/usr/bin/env python
# This python script opens the file ~/2013-10-17-uic/Metahit_index.txt 
# splits the data into columns, and prints one of the columns.

# This line needed to use the os.path.expanduser() and sys.exit() functions
import os, sys

# Build a string containing the filename 
home_dir = os.path.expanduser("~")
index_filename = os.path.join(home_dir, "2013-10-17-uic", "Metahit_index.txt")

# Try to open the file, and exit with an error if it fails
try:
    IN_FILE = open(index_filename)
except IOError:
    sys.exit("Can't open file "+ index_filename + " !")

# Loop through the lines in the file
for line in IN_FILE:
# remove end-of-line characters, then split each line at the tabs
    cols = line.rstrip().split("\t")
# cols is now a list whose elements are strings 
    sex = cols[3]
    age = cols[4]
    bmi = cols[5]
    print bmi

