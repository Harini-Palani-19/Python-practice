arr=list(map(int, input("Enter numbers:").split()))
key=int(input("Enter number to search:"))
found=False
for i in range(len(arr)):
  if arr[i]==key:
    print("Found at index",i)
    found=True
    break
if not found:
  print("Not found")
