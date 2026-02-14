a=int(input("Eter the first number:"))
b=int(input("Enter the second number:"))

while b!=0:
    a,b=b,a%b
print("GCD of two numbers is:",a)