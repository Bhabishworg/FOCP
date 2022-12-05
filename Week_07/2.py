def atleastOne(w1, w2):
    return sorted(set(w1) | set(w2))

def both(w1, w2):
    return sorted(set(w1) & set(w2))

def onlyOne(w1, w2):
    return sorted(set(w1) ^ set(w2))

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

print(f"Letters that appear in at least one of 2 words: {atleastOne(word1, word2)}\nLetters that appear in both words: {both(word1, word2)}\nLetters that appear in either word but not both: {onlyOne(word1, word2)}")
