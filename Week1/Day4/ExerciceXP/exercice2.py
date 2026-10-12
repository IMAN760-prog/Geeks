family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(name, "has to pay", price, "$")
    total += price

print("Total cost:", total, "$")


# Bonus

family = {}
number = int(input("How many family members? "))

for i in range(number):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    family[name] = age

total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(name, "has to pay", price, "$")
    total += price

print("Total cost:", total, "$")