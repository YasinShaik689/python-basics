balance = int(input("enter the amount: "))
withdraw = int(input("enter the withdraw amount: "))
if withdraw > 0:
    if balance >= withdraw:
        print("withdrawal successful")
    else:
        print("the balance is", balance)
else:
    print("invalid withdraw")
