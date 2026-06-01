
#diaplay as given output
num=int(input("Enter a number: "))

def fizz_Buzz(num):
  if num%3 == 0 and num%5 == 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    print("Fizz_Buzz")
  elif num%5 ==0:
    print("Buzz")
  elif num%3 == 0:
    print("Fizz")
  else:
    print(num)

fizz_Buzz(num)                      #function lai call garna nabirsine

#or
def fizz_Buzz(num):
  if num%5 ==0:
    print("Buzz")
  if num%3 == 0:
    print("Fizz")
  if num%3 != 0 and num%5 != 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    print("num")
  
    print(num)

fizz_Buzz(15)  

#Or
def fizz_Buzz(num):
  if num%3 == 0 and num%5 == 0:         #if-else use gare 1st condition check garera next condition ma janxa nai tara only if condition use gare ma 1st ko check garxa ra correct vaye tehi stop garxa navaye matera next if conditon ma shift hunxa
    return "num"
  if num%5 ==0:
    return "Buzz"
  if num%3 == 0:
    return "Fizz"