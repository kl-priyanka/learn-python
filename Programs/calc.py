print("This is a calculator")
i = 1
while i > 0 :
  print("Enter any two numbers : ")
  a = float(input())
  b = float(input())
  print("Choose any of the following : \n1.Add\n2.Sub\n3.Div\n4.Mul\n5.Exit\n")
  n = int(input())
  if n == 1 :
    print(a+b)
  elif n == 2 :
    print(a-b)
  elif n == 3 :
    print(a/b)
  elif n == 4 :
    print(a*b)
  elif n == 5 :
    i = -1
  else : 
    print("Wrong Input")
print("Exited the program")
