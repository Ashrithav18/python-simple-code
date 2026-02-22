arr=[1,2,2,3,4,4,5,6,7]
duplicate=[]

for num in arr:
    if arr.count(num)>1 and num not in duplicate:
        duplicate.append(num)
print("Duplicates are:",duplicate)