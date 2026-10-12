
import random

def get_random_temp(season=None):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(10, 25)
    elif season == "summer":
        return random.randint(20, 40)
    elif season == "autumn" or season == "fall":
        return random.randint(10, 25)
    else:
        return random.randint(-10, 40)


def main():
    season = input("Enter a season (summer, autumn, winter, spring): ").lower()

    temperature = get_random_temp(season)

    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature <= 23:
        print("The weather is mild. Enjoy your day!")
    elif temperature <= 32:
        print("It's warm outside. Stay hydrated!")
    else:
        print("It's really hot! Drink plenty of water.")


main()
