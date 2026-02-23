def sum_of_divisors(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=1
    return total

num1=int(input("Enter firdt number: "))
num2=int(input("Enter second number:"))

if sum_of_divisors(num1)==num2 and sum_of_divisors(num2)==num1:
    print("Amicable numbers")
else:
    print("Not Amicable numbers")