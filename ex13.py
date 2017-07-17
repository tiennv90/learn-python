from sys import argv

# This is an "import" that adds functions to Python.
# The functions constitute a "module" of code.
# (Modules can also be called "libraries.")
# "argv" is the "argument variable" that holds
# variables that you send in (or "pass") to Python.

script, first, second, third = argv
# This line "unpacks" argv into your variables 
# from left to right

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is: ", second)
print ("Your third variable is:",third)

# When you run this script, type the information for
# the variables on the same line as "python ex13.py"
# examples:
#     python ex13.py one_thing two_thing three_thing



