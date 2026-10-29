year = int(input("Enter year of service: "))
salary = float(input("Enter salary: "))
if year > 5:
    print("Bonus:", salary * 0.05)
elif year >= 2:
    print("Bonus:", salary * 0.02)
else:
    print("No bonus.")
