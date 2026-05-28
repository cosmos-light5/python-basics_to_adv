products={
    "laptop":70000,
    "mouse":500,
    "keyboard":1200,
    "monitor":1500,
}
count=0
for key, value in products.items():
    if value>1000:
        count+=1
print(f"{count} products cost more than 1000.")

#Multiplication of 3
""" count=0
for i in range (20):
    count+=1
    3*i= """



#basic dictionary comprehension
cube = {x: x**3 for x in range(10)}
print(cube)


cube = {x: x**3 for x in range(10) if 6 != x}
print(cube)


#reverse
original={"a":1, "b":2, "c":3}

swapped={key:value for key in original if value == key}



#key, value = value, key
print(swapped)