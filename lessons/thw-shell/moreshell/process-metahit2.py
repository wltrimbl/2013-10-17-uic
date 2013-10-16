#!/usr/bin/env python
# This python script opens the file ~/2013-10-17-uic/Metahit_index.txt 
# and splits the data into columns. 

# Your mission:  count the number of male, female, and neither-male-nor-
# female participants in this study in the second column.

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

numberofmale = 0
numberoffemale = 0
numberofneither = 0

# Loop through the lines in the file
for line in IN_FILE:
# remove end-of-line characters, then split each line at the tabs
    cols = line.rstrip().split("\t")
    sex = cols[3]
#    print sex   # this isn't what you actually want to do

# Print the totals 
print "Number of male:    " , numberofmale
print "Number of female:  " , numberoffemale
print "Number of neither: " , numberofneither
