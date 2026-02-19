import math

a=int(input("Enter the value  of a:"))
b=int(input("Entere the value od b:"))

if math.gcd(a,b)==1:
    print("numbers are coprime")
else:
    print("numbers are not coprime")