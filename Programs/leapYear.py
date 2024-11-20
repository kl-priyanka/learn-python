year = int(input("Enter an year : "))
if (year%100 == 0) & (year%400==0) :
  print("Leap Year")
elif (year%100 != 0) & (year%4==0) :
  print("Leap Year")
else :
  print("Not a Leap Year")
