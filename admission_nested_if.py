marks = int(input("enter the marks: "))
attendance = float(input("enter the attendance: "))
if marks >= 85:
    if attendance >= 75:
        print("Eligible for admission")
    else:
        print("Attendance is low")
else:
    print("Not eligible for admission")
