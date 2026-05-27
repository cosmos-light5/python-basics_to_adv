#set operation
""" -union(): returns a new set with elements from both sets
    -| operator: Alternative syntax for union
    -update():In-place union(modifies the original set)
    -|= operator: Alternative syntax for update
 """

set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

union=set1.union(set2)          #.union() method
print(union)

uni=set1|set2     #| operator for alternative of union;   '| --> pipe'
print(uni)