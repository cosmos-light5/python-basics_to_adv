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


  count=0
for count in range(0,7):
  count+=1
  if count==1:
    print(f"Day {count}: Gym Day")
  elif count==3 or count==5:
    print(f"Day {count}: Study Day")
  elif count==6 or count==7:
    print(f"Day {count}: Weekend! Rest Day")
  else:
    print(f"Day {count}: Work Day")

""" output:
        Day 1: Gym Day
        Day 2: Work Day
        Day 3: Study Day
        Day 4: Work Day
        Day 5: Study Day
        Day 6: Weekend! Rest Day
        Day 7: Weekend! Rest Day"""