digit = int(input("enter a digit: "))
digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
if 0 <= digit <= 9:
    print(digit_names[digit])
else:
    print("Invalid Digit")
