"""Program that outputs one of at least four random, good fortunes."""

__author__ = "73044567"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")
a = (randint(1, 4))
if a == 1:
    print("Try new things, and remember we all start somewhere")
else: 
    if a == 2:
        print("Success is relative, so find what it means to you")
    else: 
        if a == 3:
            print("Bloom where you're planted")
        else: 
            print("Allow your failures to provide insight rather than defeat")
print("Now, go spread positive vibes!")
    
