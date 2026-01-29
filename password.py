password=input("Enter Password:")
if len(password)<8:
  print("Weak")
elif any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password):
  print("Strong")
else:
  print("Medium")
