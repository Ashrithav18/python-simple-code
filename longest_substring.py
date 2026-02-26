s = input("Enter a string: ")

longest = ""
current = ""

for char in s:
    if char not in current:
        current += char
    else:
        if len(current) > len(longest):
            longest = current
        current = char

if len(current) > len(longest):
    longest = current

print("Longest substring:", longest)