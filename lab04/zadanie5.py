sentence = input("Podaj zdanie: ")
words = sentence.split()
sorted_words = sorted(words, key=len)
print("Posortowane wyrazy według długości:")
for word in sorted_words:
    print(word)