arr=[4,7,2,5,6,9]
is_sorted= True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("The numbers are sorted")
else:
    print("The given numbers are not sorted")
        
