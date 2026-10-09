
word = input("Enter a word: ")
result = ""

for letter in word:
    if result == "" or letter != result[-1]:
        result += letter

print(result)
