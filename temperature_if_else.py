temperature = int(input("enter the temperature: "))
if temperature >= 40:
    print("Weather is too hot")
elif temperature >= 35:
    print("Weather is hot")
elif temperature >= 25:
    print("Weather is warm")
elif temperature >= 15:
    print("Weather is cool")
else:
    print("Weather is cold")
