num=int(input("Enter a number:"))
temp=num
digit=str(num)

sum_val=0

for i in range(len(digit)):
    sum_val+=int(digit[i])**(i+1)
    
if sum_val==num:
    print("Disarium Number")
else:
    print("Not a Disarium number")