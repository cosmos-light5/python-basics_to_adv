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