number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []
i = 1

while True:
    multiples.append(number * i)
    i += 1

    if i > length:
        break

print(multiples)