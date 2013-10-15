#!/usr/bin/env python
# This python script opens the file ~/2013-10-17-uic/Metahit_index.txt 
# and splits the data into columns.

# Your mission:  count the number of individuals with BMI's <=30
# and those with BMI's > 30 or undefined.

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

numbertoinclude = 0
numbertoexclude = 0

# Loop through the lines in the file
for line in IN_FILE:
# remove end-of-line characters, then split each line at the tabs
    cols = line.rstrip().split("\t")
    sex = cols[3]
    bmi = cols[5]
#    print bmi   # this isn't what you actually want to do

# Print the totals 
print "Number BMI <= 30 :           " , numbertoinclude 
print "Number BMI > 30 or unknown:  " , numbertoexclude
