marks = int(input("enter the marks: "))
attendance = int(input("enter the attendance: "))
if marks < 85:
    print("not eligible for admission")
elif attendance < 75:
    print("not eligible for admission")
else:
    print("eligible for admission")
