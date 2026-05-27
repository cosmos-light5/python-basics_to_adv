#set operation
""" -union(): returns a new set with elements from both sets
    -| operator: Alternative syntax for union
    -update():In-place union(modifies the original set)
    -|= operator: Alternative syntax for update
 """

""" set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

union=set1.union(set2)          #.union() method
print(union)
#equivalent method
uni=set1|set2     #| operator for alternative of union;   '| --> or'
print(uni)


set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

upd=set1.update(set2)       #updated elements will be stored either in assumed variable or in set1 i.e. in set just before .update(), not in parenthesis of update()
print(upd)                  #incorrect way
#Output: None --> because upd variable le hold garne value nai paudain kina vane set1.update(set2) aafai ma value hold gardaia, matra operation ho, so khali hunxa upd set

set1.update(set2)       #updated elements will be stored either in assumed variable or in set1 i.e. in set just before .update()
print(set1)             #Output:{0,1,2,3,4,5,6,7,8,9,0,11,12}  i.e. original set1 lai nai change garne raixa..
#equivalent method
set1|=set2 #            #two sets ma update ra |= operator use gare tesle original set change garne vayeko le operate garda aaune 1st set print garne, but multi-union garda chai variable ma rakhera pani garna milxa
print(set1)

#multi-union
set1={1,3,9,11,12}
set2={6,8,0,11,12}
set3={2,4,5,7}

multi_union=set1.union(set2,set3)
print(multi_union)                  #Output:{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}

#OR operator
multi_uni=set1|set2|set3
print(multi_uni) """

#Intersection
""" -intersection(): returns a new set with elements common to both sets
    -& operator: Alternative syntax for intersection
    -intersection_update(): In-place intersection (modifies the original set)
    -&= operator: Alternative syntax for intersection_update"""

""" set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

common=set1.intersection(set2)          #variable ma intersection nai name chahi narakhne because its one of the pre defined key-words ho
print(common)                       #Output:{11, 12}

common=set1 & set2
print(common)                       #Output:{11, 12}

#Intersection_update()
set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

set1.intersection_update(set2)
print(set1)                         #Output:{11, 12}

#equivalent and-equals method
set1 &= set2 #
print(set1)                         #Output:{11, 12}

#multiple intersection
set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}
set3={11,8,9,13,24}

multiple_intersection=set1.intersection(set2,set3)
print(multiple_intersection)                #Output: {11}

#eqv method
multi_intsec= set1 & set2 & set3
print(multi_intsec)                         #Output: {11}
 """
#set operation: Difference
""" -difference(): returns a new set with elements in the first set but not in second set
    - -operator: Alternative syntax for difference
    - difference_update(): In-place difference(modifies the original set)
    - -= operator: Alternative syntax for difference_update
"""

""" set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

sub=set1.difference(set2)
print(sub)              #Output:{1, 3, 5, 7, 9}

diff=set1-set2
print(diff)             #Output: {1, 3, 5, 7, 9}

#set difference_update method
set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

set1.difference_update(set2)
print(set1)             #Output: {1, 3, 5, 7, 9}

#eqv method
set1 -= set2 #
print(set1)             #Output: {1, 3, 5, 7, 9}


#multi set difference
set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}
set3={11,8,9,13,24}

set1.difference_update(set2,set3)
print(set1)             #output: {1, 3, 5, 7}

 """
#Symmetric difference
""" -symmetric_difference(): returns element in either set, but not in both
    -^ operator: alternative syntax for symmetric_difference
    -symmetric_difference_update(): In-place operation
    -^= operator: Alternative syntax for symmetric_difference_update
"""

set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

sym_diff=set1.symmetric_difference(set2)
print(sym_diff)


set1^=(set2)    #^-->carate symbol; ^ not power operator but ** is.
print(set1)



#frozenset
