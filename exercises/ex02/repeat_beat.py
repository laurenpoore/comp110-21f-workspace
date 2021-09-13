"""Repeating a beat in a loop."""

__author__ = "73044567"


# Begin your solution here...

beat: str = str(input("What beat do you want to repeat? "))
number_of_repeats: int = int(input("How many times do you want to repeat it? "))
counter = 0

while counter < number_of_repeats:
    counter = counter + 1
    if counter == number_of_repeats:
        print(((number_of_repeats - 1) * (beat + " ")) + (beat))
        counter = counter + 1

if number_of_repeats <= 0:
    print("No beat...")