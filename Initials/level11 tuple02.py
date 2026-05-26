#tuple conversion
num=[1,3,4,5,7,9,0]
tuple_conversion=tuple(num)
indexed_conversion=tuple(enumerate(num))
print(tuple_conversion)
print(indexed_conversion)         #(0,1) first ko index ho next chai index ko corresponding value

#sample question
students = [
    ("Alice", 20, "A"),
    ("Bob", 19, "B"),
    ("Charlie", 21, "A"),
    ("David", 20, "C")
]

for i, stud in enumerate(students):
  for j, grade in enumerate(stud):
    if grade == "A":
      print(stud)               #yo hard type code ho, yesari nagarne



#1st better way
students = [
    ("Alice", 20, "A"),
    ("Bob", 19, "B"),
    ("Charlie", 21, "A"),
    ("David", 20, "C")
]
for stud in students:
  if stud[2] == "A":
    print(stud)
    

#2nd but best way
for name, age, grade in students:
  if grade=="A":
    print(students)


""" Why to use tuple?
-Immutability: Tuples cannot be modified after creation, which can help prevent accidental changes to data.
-Performance: Tuples are generally faster than lists of read-only operations
-Hashability: Tuples can be used as keys in dictionaries, while lists cannot.
-Data Integrity: Prorect data that should not be changed, such as coordinates or fixed sets of values.
-perfect for representing fixed collections of items, such as RGB color values or database records."""


name="ram"
student=(('name',name),('age', 10),('grade', 5))
print(student)

""" Output:
(('name', 'ram'), ('age', 10), ('grade', 5))"""