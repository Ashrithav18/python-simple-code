import math
num=int(input("Enter number:"))
temp=num
total=0

while temp>0:
    digit=temp%10
    total+=math.factorial(digit)
    temp//=10
if total==num:
    print("The nuber is strong number")
else:
    print("The number is not strong number")