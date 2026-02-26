numbers = [2,2,1,2,3,2,2]

majority = None

for num in numbers:
    if numbers.count(num) > len(numbers)//2:
        majority = num
        break

if majority:
    print("Majority element:", majority)
else:
    print("No majority element")