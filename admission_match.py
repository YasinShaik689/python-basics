marks = float(input("enter marks: "))
attendance = float(input("enter attendance percentage: "))
match marks:
    case marks if marks < 75:
        print("Not eligible")
    case _ if attendance < 75:
        print("Not eligible")
    case _:
        print("Eligible for admission")
