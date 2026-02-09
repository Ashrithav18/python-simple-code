
num=int(input("Enter the number to find the sum of it: "))
total=0
while num>0:
    digit=num%10
    total+=digit
    num//=10

print("The sum of the given number is:",total)
#feb 9