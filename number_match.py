number = int(input("Enter a number (1-3): "))
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid choice")
