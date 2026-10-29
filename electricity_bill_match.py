units = float(input("enter units consumed: "))
match units:
    case units if units <= 100:
        bill = units * 2
    case units if units <= 200:
        bill = units * 3
    case _:
        bill = units * 5
print("Electricity bill:", bill)
