arr=list(map(int, input("Enter numbers: ").split()))
largest=arr[0]
smallest=arr[0]
for num in arr:
  if num>largest:
    largest=num
  if num<smallest:
    smallest=num
print("Largest: ",largest)
print("Smallest: ",smallest)
