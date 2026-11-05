#how to fix the IndexError: list index out of range error when we run the script without passing the second argument
import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments") # exit the script with a non-zero exit code to indicate an error
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") # exit the script with a non-zero exit code to indicate an error

print("Hello", sys.argv[1]) # if we run the script with python 03-sys.py David we get Hello, David    