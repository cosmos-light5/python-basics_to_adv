#practice with for loop, continue and break statements
num=int(input("enter a number: "))
count=0

for count in range(0,num):
  count+=1
  if count%3 == 0:
    continue
  if count>=20:
    break
  print(count)


#practice with while loop, continue and break statements
number=int(input("enter a number: "))
count=0
while count<=number:
  count+=1
  if count%3 == 0:
    continue
  if count>=20:
    break
  print(count)