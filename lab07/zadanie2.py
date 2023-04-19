words = input("Podaj listę wyrazów oddzielonych spacją: ").split()
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print("Posortowane wyrazy:", sorted_words)