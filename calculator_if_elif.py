num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
choice = int(input("Enter your choice (1-6): "))
if choice == 1:
    print("Addition:", num1 + num2)
elif choice == 2:
    print("Subtraction:", num1 - num2)
elif choice == 3:
    print("Multiplication:", num1 * num2)
elif choice == 4:
    print("Division:", num1 / num2)
elif choice == 5:
    print("Modulus:", num1 % num2)
elif choice == 6:
    print("Exponent:", num1 ** num2)
else:
    print("Invalid choice.")
