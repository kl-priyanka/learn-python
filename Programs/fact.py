num = int(input("Enter a positive integer : "))
fact = 1
if num < 0 :
  print("Not valid")
  exit()
else : 
  for i in range(1,num+1) :
    fact = fact * i
print(fact)
