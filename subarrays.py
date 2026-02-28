numbers = [1,2,3]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        print(numbers[i:j+1])