#set intro
""" -an unordered collection of unique elements 
    -unordered (items have no defined order, you cannot access items by index)
    -no redundant items (each item is unique, duplicates are removed automatically)
    -elements must be immutable (cannot be changed after creation, e.g. numbers, strings, tuples but not lists or dictionaries)
    -sets are mutable (you can add or remove items from a set after it is created)
    -fast membership testing [o(1) average time complexity for checking if an item is in a set]
    -created using curly braces {} or the set() constructor i.e.
                syntax:set_name = {item1, item2, item3} or set_name = set([item1, item2, item3])
    -common operations: union, intersection, difference, symmetric difference"""

empty=set()       #set{} --> creates dictionary so use ()
print(empty)


str=("hello, welcome to nepal..")
str_set=set("hello, welcome to nepal..")
print(str)
print(str_set)