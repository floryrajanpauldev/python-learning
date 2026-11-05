#how to fix the IndexError: list index out of range error when we run the script without passing the second argument
import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments") # exit the script with a non-zero exit code to indicate an error

for arg in sys.argv[1:]:
    print("Hello", arg) # if we run the script with python 03-sys.py David John Mike" 
    #output using slice notation sys.argv[1:]
    # Hello David
    # Hello John
    # Hello Mike

for arg in sys.argv[1:-1]:
    print("Hello", arg) # if we run the script with python 03-sys.py David John Mike" 
    #output using slice notation sys.argv[1:]
    # Hello David
    # Hello John
