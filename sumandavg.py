arr = list(map(int, input("Enter numbers: ").split()))
total = 0
for num in arr:
    total += num
average = total / len(arr)
print("Sum:", total)
print("Average:", average)
