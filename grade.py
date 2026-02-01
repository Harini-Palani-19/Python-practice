total = 0
n = int(input("How many subjects? "))

for i in range(n):
    marks = int(input(f"Enter marks {i+1}: "))
    total += marks

avg = total / n

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "D"

print("Average =", avg)
print("Grade =", grade)
