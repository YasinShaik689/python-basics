balance = float(input("enter the balance amount: "))
withdraw = float(input("enter the withdrawal amount: "))
match withdraw:
    case withdraw if withdraw <= 0:
        print("Invalid withdrawal amount")
    case withdraw if withdraw > balance:
        print("Insufficient balance")
    case _:
        balance -= withdraw
        print("Withdrawal Successful")
        print("remaining balance:", balance)
