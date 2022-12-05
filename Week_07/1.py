def letter(string):
    letters = set(string)

    return sorted(letters)

word = input("Enter a word: ")
print(letter(word))