for j in range(0,5):
    for s in range(0,5-j-1):
        print(" ",end="  ")
    for i in range(j,-1,-1):
        print(i+1,end="  ")
    print(" ",end="\n")