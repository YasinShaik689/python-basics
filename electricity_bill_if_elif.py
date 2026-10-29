units = int(input("enter the number of units used: "))
if units <= 100:
    print("the amount charged is:", units * 2)
elif units <= 200:
    print("the amount charged is:", units * 3)
else:
    print("the amount charged is:", units * 5)
