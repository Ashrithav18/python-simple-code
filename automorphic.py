num=int(input("Enter the number:"))
square=num*num
if str(square).endswith(str(num)):
    print("The number is Automorphic")
else:
    print("The number is not Automorphic")