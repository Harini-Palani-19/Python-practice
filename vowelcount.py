str1=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for ch in str1:
  if ch in vowels:
    count+=1
print("Vowels:",count)    
