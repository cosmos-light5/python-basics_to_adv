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
    print(stud[0])
