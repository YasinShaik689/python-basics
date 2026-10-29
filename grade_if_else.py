marks = [int(input(f"enter marks of subject {subject}: ")) for subject in range(1, 6)]
average = sum(marks) / 5
print("Average=", average)
if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
else:
    print("Grade F")
