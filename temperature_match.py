temperature = int(input("enter the temperature: "))
match temperature:
    case temperature if temperature >= 40:
        print("Weather is too hot")
    case temperature if temperature >= 35:
        print("Weather is hot")
    case temperature if temperature >= 25:
        print("Weather is warm")
    case temperature if temperature >= 15:
        print("Weather is cool")
    case _:
        print("Weather is cold")
