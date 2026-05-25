#Tuple
""" -immutable: once created, cannot be modified (no add, remove, or change elements)
   -ordered: maintains the order of elements as they were defined
   -allows duplicates: can contain duplicate values
   -can contain different data types: can hold a mix of data types (e.g., integers, strings, etc.)
   -defined using parentheses: created using parentheses () or the tuple() constructor
   -supports indexing and slicing: can access elements using indexing and slicing
   -hashable: can be used as keys in dictionaries or elements in sets (if all elements are hashable)
   -use cases: used for fixed collections of items, such as coordinates, RGB values, or any data that should not be modified after creation
   -performance: generally faster than lists for certain operations due to immutability
   -memory efficiency: typically uses less memory than lists due to immutability
   -methods: supports methods like count() and index(), but does not support methods that modify the tuple (e.g., append(), remove())
   -packing and unpacking: can pack multiple values into a tuple and unpack them into variables
   -nested tuples: can contain other tuples as elements, allowing for complex data structures
   -can be used as keys in dictionaries: since tuples are immutable, they can be used as keys in dictionaries, while lists cannot
   -can be used in sets: tuples can be added to sets, while lists cannot due to their mutability"""

#empty tuple
empty_tuple = ()
print(empty_tuple)

#single element tuple (note the comma)
single_element_tuple = (42,)            #without the comma, it would be just an integer inside parentheses, not a tuple
print(single_element_tuple)         # Output: (42,)

tuple=(42)  #this is not a tuple, it's just an integer
print(tuple)             # Output: 42

num=(1, "hello", 3.14, True)
print(num)              # Output: (1, "hello", 3.14, True)

#multiple element tuple
multiple_element_tuple = (1, "hello", 3.14)
print(multiple_element_tuple)

#accessing elements
print(multiple_element_tuple[1])  # Output: "hello"

#tuple paking without parentheses
packed_tuple = 1, "hello", 3.14
print(packed_tuple)    # Output: (1, "hello", 3.14)

#tuple unpacking
a, b, c = packed_tuple
print(a)  # Output: 1
print(b)  # Output: "hello" 
print(c)  # Output: 3.14


x,y,z=(10,20,30)
print(x)  # Output: 10
print(y)  # Output: 20

#indexing and slicing, concatenation, counting, length and other operations same as lists
colors = ("red", "green", "blue", "yellow")
print(colors[0])  # Output: "red"   => indexing
print(colors[1:3])  # Output: ("green", "blue") => slicing

tuple1=(1,2,3)
tuple2=(4,5,6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

#repetition
repeated = tuple1 * 3
print(repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)      #repeating the elements of tuple1 three times



#only methods in tuple are count and index
colors = ("red", "green", "blue", "yellow")
print(colors.count("red"))  # Output: 1
print(colors.index("blue"))  # Output: 2

print(len(colors))  # Output: 4

#membership test
print("green" in colors)  # Output: True
print("purple" in colors)  # Output: False  

#using * to collect remaining elements during unpacking
numbers = (1, 2, 3, 4, 5)  
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]  (rest is a list containing the remaining elements)

#swapping values using tuple unpacking
a = 10
b = 20
a, b = b, a
print(a)  # Output: 20
print(b)  # Output: 10

