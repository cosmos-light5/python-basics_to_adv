#display patterns
""" for i in range(1,6):          #1 to 5 samma print garxa
  for j in range(i,5):        #1 to 4 samma print garxa i.e. inner loop 4 times chale paxi matra outer loop ko 1 loop complete hunxa ra 2nd loop suru hunxa total 5x4=20 times chalxa
    print("i=",i,"j=",j)

output:
i= 1 j= 1
i= 1 j= 2
i= 1 j= 3
i= 1 j= 4
i= 2 j= 2
i= 2 j= 3
i= 2 j= 4
i= 3 j= 3
i= 3 j= 4
i= 4 j= 4


for i in range(1,6):
  for j in range(1,5):
    print("*",end="")
  print()               #innerloop 4 times complete vayesi 1st outer loop complete hunxa next outer loop initiate garnu aaghi gap wa newline feed diyeko



#Displaying patterns without using nested loops
num=int(input("enter a number of rows: "))
for i in range(1,num+1):                    
  print("*"*i) 



#same pattern using nested loops
num=int(input("enter a number of rows: "))
for i in range(1,num+1):
  for j in range(1,i+1):
    print("*", end="")              #eg. 0 to 5 range ma vaye 4 wata hunthyo here 0+1 to number+1 gare ko
  print()




#just seperated with space
num=int(input("enter a number of rows: "))
for i in range(1,num+1):
  for j in range(1,i+1):
    print("*", end=" ")              #eg. 0 to 5 range ma vaye 4 wata hunthyo here 0+1 to number+1 gare ko
  print()




#reversing the above pattern
num=int(input("enter a number of rows: "))
for i in range(num,0,-1):
  for j in range(0,i):
    print("*",end="")
  print()



#reversing the above pattern with space
num=int(input("enter a number of rows: "))
for i in range(num,0,-1):
  for j in range(0,i):
    print("*",end=" ")
  print()





#piramid with space in between and sequence of consecutive increasing numbers
num=int(input("Enter number of rows: "))

for i in range(0,num):
  for j in range(0,num-i-1):            #space ko lagi
    print("",end=" ")
  for j in range(0,i+1):                #* ko lagi
    print("*",end=" ")
  print()


#right handed right angled triangle
num=int(input("Enter number of rows: "))

for i in range(0,num):
  for j in range(0,num-i-1):            #space ko lagi
    print("",end=" ")
  for j in range(0,i+1):                #* ko lagi
    print("*",end="")                   #same mathi ko code ma * ko lagi print garda end ma space nadiye righi sided right angled triangle dinxa...
  print()
"""



#piramid with no space inbetween i.e. odd no. of * in every row
for i in range(1,6):                #1 to (6-1) wata rows ma print garne vaneko xa
  for j in range(i,6):              #i le rows indicate gareko ra rows ma space ko no. diyeko
    print(" ",end=" ")
  for k in range(0,i):              #
    print("*",end=" ")
  for m in range(i,1,-1):
    print("*",end=" ")
  print(" ")