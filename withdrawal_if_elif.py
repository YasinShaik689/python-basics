balance = int(input("enter the amount: "))
withdraw = int(input("enter the withdraw amount: "))
if withdraw > 0 and balance >= withdraw:
    print("withdrawal successful")
elif balance < withdraw:
    print("the balance is", balance)
else:
    print("invalid withdraw")
