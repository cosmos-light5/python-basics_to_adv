#--> for single line comment
"""... """ -->for multi line comment
"""when semantics is displayed:
    accept --> tab, 
    accept word -->ctrl + right_arrow"""

s="ram"
f=None #f is a special constant in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value assigned to it or that a function does not return anything.
p=True
q=5j

print (s)
print (p)
print(type(f))

print(f)
print(q)
z = 3 + 4j
#z = 3i [matra lekhe decimal literal error aauxa]
# Print the whole complex number
print("Complex number:", z)
print(type(z))
# Print real and imaginary parts separately
print("Real part:", z.real)
print("Imaginary part:", z.imag) 
"""output:
ram
True
<class 'NoneType'>
None
5j
Complex number: (3+4j)
<class 'complex'>
Real part: 3.0
Imaginary part: 4.0
"""

num00=int(input()) #input without message
num2=input("no. please: ")
num3=input("no. please: ")
x=int(num2)
y=int(num3)

print("concatinated given numbers ", num2+num3)
add=x + y
print(int(add))
print("The sum of the given input is ", add) 
"""output:
2
no. please: 5
no. please: 3
concatinated given numbers  53
8
The sum of the given input is  8
"""