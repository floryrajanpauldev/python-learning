#sys — System-specific parameters and functions¶

import sys
# we can use sys.argv to get the command line arguments passed to the script
# sys.argv is a list of command line arguments passed to the script
# the first argument is always the name of the script
print("My name is 1- ", sys.argv[0]) # run the file with python 03-sys.py David to see the output

print("My name is 2- ", sys.argv[1]) # if we run without the name David we get IndexError: list index out of range because we are trying to access the second argument which is not passed to the script

"""
Output:
My name is 1-  /Users/floryrajanpaul/Documents/python-learning/harvard-cs50p/05-modules-libraries/03-sys.py
My name is 2-  David
"""

