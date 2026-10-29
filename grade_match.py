marks = [int(input(f"enter marks of subject {subject}: ")) for subject in range(1, 6)]
average = sum(marks) / 5
print("Average=", average)
match average:
    case average if average >= 90:
        print("Grade A")
    case average if average >= 80:
        print("Grade B")
    case average if average >= 70:
        print("Grade C")
    case average if average >= 60:
        print("Grade D")
    case _:
        print("Grade F")
