list1=[1,3,4,5,7]
list2=[1,6,9,0,4]
common=[]
for num in list1:
    if num in list2:
        common.append(num)
print(common)