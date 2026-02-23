num=int(input("Enter a number: "))
while num>9:
    sum_digits=0
    while num >0:
        sum_digits+=num%10
        num=num//10
        
    num=sum_digits
print("single digit:",num)