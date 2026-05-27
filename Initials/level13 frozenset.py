#Frozenset
""" -an immutable version of set
    -Key differences from set:
     -cannot be changed after creation (no add, remove, update) 
     -can be used as dictionary keys or as elements of another sets
     -All non-modifying set operations stil work
     -creating a frozenset: 
            use frozen() constructor"""

#set vitra set rakhna mildaina tara frozenset rakhna milxa due to its immutability

a=frozenset({1,2,2})
print(a)
print(type(a))
""" Output:
frozenset({1, 2})
<class 'frozenset'>
 """

b=a.union({4,5,6})
print(b)
""" Ouput: frozenset({1, 2, 4, 5, 6}) """


#using frozenset as a dictionary key
fs1=frozenset({1,2,3})
fs2=frozenset({4,5,6})

set_dict={fs1:"Group1",fs2:"Group2"}
print(set_dict)
""" Output: {frozenset({1, 2, 3}): 'Group1', frozenset({4, 5, 6}): 'Group2'} """



#using frozenset as an element in set
set_of_frozenset={fs1,fs2}
print(set_of_frozenset)
""" Output: {frozenset({1, 2, 3}), frozenset({4, 5, 6})} """