"""

Reverse a String - Enter a string and the program will reverse it and print it out. 

"""

import sys

try:
    arg1 = sys.argv[1]
except ValueError:
    sys.exit("One input string is required")

print list(reversed(arg1))
