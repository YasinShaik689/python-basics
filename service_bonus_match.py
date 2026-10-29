year = int(input("Enter year of service: "))
salary = float(input("Enter salary: "))
match year:
    case year if year > 5:
        print("Bonus:", salary * 0.05)
    case year if year >= 2:
        print("Bonus:", salary * 0.02)
    case _:
        print("No bonus.")
