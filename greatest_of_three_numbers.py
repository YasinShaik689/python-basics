number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("enter the third number: "))
if number1 > number2:
    if number1 > number3:
        print("first number is greater")
    else:
        print("third number is greater")
else:
    print("second number is greater")
