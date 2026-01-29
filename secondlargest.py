nums = list(set(map(int, input("Enter numbers: ").split())))
nums.sort()

print("Second largest:", nums[-2])
