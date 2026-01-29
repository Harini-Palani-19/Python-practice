nums = list(map(int, input("Enter numbers: ").split()))
unique = []

for x in nums:
    if x not in unique:
        unique.append(x)

print(unique)
