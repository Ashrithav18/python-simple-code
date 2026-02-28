list1 = [1,2,3,4]
list2 = [3,4,1,2]

if len(list1) == len(list2) and str(list2) in str(list1 * 2):
    print("Rotation of each other")
else:
    print("Not rotation")