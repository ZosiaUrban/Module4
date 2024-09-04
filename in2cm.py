iTc=2.54
while True:
 n=float(input("Enter lenght in intches "))
 if n > 0:
       n = n * iTc
       print(f"that is {n} cm")
 elif n < 0:
  print("cant convert a negative number")
  break 