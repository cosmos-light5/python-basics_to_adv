#Dictionaries
""" -An unorderes, mutable collection of key-value pairs 
Key characteristics:
    -keys must be unique and immutable (string, number, tuples). values can be of any data-type and can be duplicated
    -unordered in python<3.7(ordered by insertion since 3.7+)
    -Mutable (can be changed after creation)
    -Fast lookups by key (O(1)) average case
    -syntax:
            created using {} with key-value pairs
"""
empty_dict={}
print(empty_dict)

#keys cannot be list or set but values can
mixed_dict={"str_key":"value", "int_key":55, "list_key":[1,7,0]}
print(mixed_dict)

#dict() implementation
using_dict_function=dict(name="Yak-dai", age=25, city="Shangri-la")
print(using_dict_function)

from_tuples=dict([("name","Yak-dai"), ("age",25), ("city","Shangri-la")])
print(from_tuples)



books={"Title":"Radha",
       "Auther":"Krishna Dharabasi",
       "Price":450}
print(books)


