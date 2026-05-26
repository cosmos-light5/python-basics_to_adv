#tuple conversion
num=[1,3,4,5,7,9,0]
tuple_conversion=tuple(num)
indexed_conversion=tuple(enumerate(num))
print(tuple_conversion)
print(indexed_conversion)         #(0,1) first ko index ho next chai index ko corresponding value
""" Output:
(1, 3, 4, 5, 7, 9, 0)
((0, 1), (1, 3), (2, 4), (3, 5), (4, 7), (5, 9), (6, 0)) """


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
""" Output:
('Alice', 20, 'A')
('Charlie', 21, 'A')"""


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
""" Output:
('Alice', 20, 'A')
('Charlie', 21, 'A')"""


#2nd but best way
for name, age, grade in students:           #range or len use garera pani garna sakincha
  if grade=="A":
    print(name, age, grade)
""" Output:
Alice 20 A
Charlie 21 A"""

""" Why to use tuple?
-Immutability: Tuples cannot be modified after creation, which can help prevent accidental changes to data.
-Performance: Tuples are generally faster than lists of read-only operations
-Hashability: Tuples can be used as keys in dictionaries, while lists cannot.
-Data Integrity: Prorect data that should not be changed, such as coordinates or fixed sets of values.
-perfect for representing fixed collections of items, such as RGB color values or database records."""


name="ram"
student=(('name',name),('age', 10),('grade', 5))
print(student)
print(student[0][1])  # Output: ram
""" Output:
(('name', 'ram'), ('age', 10), ('grade', 5))"""

#last Question
students = [
    ("Alice", 20, "A"),
    ("Bob", 19, "B"),
    ("Charlie", 21, "A"),
    ("David", 20, "C")
]

studs=[]
for stud in students:
  if (stud[2]=="A"):
    studs.append(stud[0])
print(studs)   # Output: ['Alice', 'Charlie']
  