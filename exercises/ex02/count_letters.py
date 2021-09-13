"""Counting letters in a string."""

__author__ = "730444567"


# Begin your solution here...

letter_search: str = str(input("What letter do you want to search for?: "))
word_selection: str = str(input("Enter a word: "))
counter = 0
iteration = 0
while (iteration < len(word_selection)):
    if(word_selection[iteration] == letter_search):
        counter = counter + 1
    iteration = iteration + 1
print("Count: ", counter)
