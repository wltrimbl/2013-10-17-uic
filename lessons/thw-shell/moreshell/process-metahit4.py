#!/usr/bin/env python
# This python script opens the file ~/2013-10-17-uic/Metahit_index.txt 
# for input, splits the data into columns, and loops through the it.
# It also opens Metahit_include.txt and Metahit_exclude.txt for output.

# Your mission:  output individuals with BMI <= 30 into the one file
# (Metahit_include.txt) and with BMI > 30 to the other file 
# (Metahit_exclude.txt)

# This line needed to use the os.path.expanduser() and sys.exit() functions
import os, sys

# Build a string containing the filename 
home_dir = os.path.expanduser("~")
index_filename = os.path.join(home_dir, "2013-10-17-uic", "Metahit_index.txt")
out_exclude_filename = os.path.join(home_dir, "2013-10-17-uic", "Metahit_include.txt")
out_include_filename = os.path.join(home_dir, "2013-10-17-uic", "Metahit_exclude.txt")

# Try to open the file, and exit with an error if it fails
try:
    IN_FILE = open(index_filename)
except IOError:
    sys.exit("Can't open file "+ index_filename + " !")

# Open the two output files
OUT_INCLUDE = open(out_include_filename, "w")
OUT_EXCLUDE = open(out_exclude_filename, "w")

# Loop through the lines in the file
for line in IN_FILE:
# remove end-of-line characters, then split each line at the tabs
    cols = line.rstrip().split("\t")
    sex = cols[3]
    age = cols[4]
    bmi = cols[5]
    # your code here

# close the two output files
OUT_INCLUDE.close()
OUT_EXCLUDE.close()

