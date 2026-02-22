list1=[1,2,3,4,5,6]
list2=[1,2,4,6,8,9,10,17,12,34]
merged=list1+list2
unique=[]
for num in merged :
    if num not in unique:
        unique.append(num)
print(unique)