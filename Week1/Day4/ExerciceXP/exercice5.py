import random
def Numbers():
    numbers = int(input("Entre a numbre betwen 1 and 100: "))
    number = random.randint(1,100)
    if numbers == number:
        print("Very good")
    else:
        print("Good luck! The numbers are:", numbers, number)
Numbers()   
    


