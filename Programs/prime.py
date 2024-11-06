a = int(input("Enter an integer : "))
flag = 0
if (a == 0) | (a == 1) :
    print("Not a prime number")
else :
    for i in range(2,a) :
      if (a%i) == 0 :
        flag = True
if flag :
    print("Not a Prime Number")
else :
    print("Prime number")
