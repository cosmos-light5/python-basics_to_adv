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
 """
""" output:
        Day 1: Gym Day
        Day 2: Work Day
        Day 3: Study Day
        Day 4: Work Day
        Day 5: Study Day
        Day 6: Weekend! Rest Day
        Day 7: Weekend! Rest Day

#to print in descending order
num=int(input("Enter a number: "))
count=0

for count in range(num,0,-1):
  print(count)



# to print in number in reverse order and check palindrome

num = int(input("Enter a number: "))
original_num = num
rev_num = 0

for i in str(num):        # convert number to string only to know loop length
    rem = num % 10
    num //= 10
    rev_num = rev_num * 10 + rem

print("Reverse of the given number:", rev_num)

if original_num == rev_num:
    print("Entered number is palindrome.")
else:
    print("Entered number is not palindrome.")



#OR
number = input("Enter the number to check: ")

rev_number = ""

for digit in number:        # Reverse the string using a for loop
    rev_number = digit + rev_number

print(f"Reverse of the given number = {rev_number}")
if number == rev_number:
    print("Entered number is palindrome.")
else:
    print("Entered number is not palindrome.")


#OR
def check_and_reverse_palindrome(n):    
    str_num = str(n)

      reversed_str = str_num[::-1]        # Reverse the string using slicing

    if str_num == reversed_str:
        print(f"{n} is a palindrome!")
        print(f"Reversed: {reversed_str}")
        return True                         #use of return true or false, only works inside a function
    else:
        print(f"{n} is NOT a palindrome.")
        print(f"Reversed: {reversed_str}")
        return False
    
check_and_reverse_palindrome(12321)