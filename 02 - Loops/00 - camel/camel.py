camelCase = input("camelCase: ")

for character in camelCase:
    if character.isupper():
        print("_" + character.lower(), end="")
    else:
        print(character, end="")
print()