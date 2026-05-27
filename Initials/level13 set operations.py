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
#equivalent method
uni=set1|set2     #| operator for alternative of union;   '| --> pipe'
print(uni)


set1={1,3,5,7,9,11,12}
set2={2,4,6,8,0,11,12}

upd=set1.update(set2)       #updated elements will be stored either in assumed variable or in set1 i.e. in set just before .update()
print(upd)                  #incorrect way
#Output: None --> because upd variable le hold garne value nai paudain kina vane set1.update(set2) aafai ma value hold garne hoina matra operation ho, so khali hunxa upd set

set1.update(set2)       #updated elements will be stored either in assumed variable or in set1 i.e. in set just before .update()
print(set1)             #Output:{0,1,2,3,4,5,6,7,8,9,0,11,12}  i.e. original set1 lai nai change garne raixa..
#equivalent method
set1|=set2              #update ra |= operator le original set change garne vayeko le operate garda aaune 1st set print garne
print(set1)

#multi-union
set1={1,3,9,11,12}
set2={6,8,0,11,12}
set3={2,4,5,7}

multi_union=set1.union(set2,set3)
print(multi_union)                  #Output:{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}