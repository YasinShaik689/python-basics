attendance = float(input("enter the percentage of attendance: "))
income = int(input("enter the income: "))
if income < 200000 and attendance > 75:
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")
