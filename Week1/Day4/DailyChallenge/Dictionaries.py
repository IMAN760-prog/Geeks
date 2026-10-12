
word = input("Enter a word: ")

letters = {}

for index, letter in enumerate(word):
    if letter not in letters:
        letters[letter] = []

    letters[letter].append(index)

print(letters)
