"""Relational Operators"""

__author__ = "730444567"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input ("Right-hand side: "))
left_less_than_right: bool = 6 < 8
left_greater_equal_to_right: bool = 6 >= 8
left_equal_right: bool = 6 == 8
left_not_equal_right: bool = 6 != 8

print("6 " + "< " + "8 " + "is " + str(left_less_than_right))
print("6 " + ">= " + "8 " + "is " + str(left_greater_equal_to_right))
print("6 " + "== " + "8 " + "is " + str(left_equal_right))
print("6 " + "!= " + "8 " + "is " + str(left_not_equal_right))