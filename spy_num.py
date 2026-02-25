num=int(input("Enter the number:"))
temp=num
sum_digits=0
product=1
while temp>0:
    digit=temp%10
    sum_digits+=digit
    product*=digit
    temp//=10
if sum_digits==product:
    print("Spy number")
else:
    print("Not a Spy number")