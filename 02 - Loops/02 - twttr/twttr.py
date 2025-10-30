input = input("Input: ")
vowels = 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'

for character in input:
    if character not in vowels:
        print(character, end="")