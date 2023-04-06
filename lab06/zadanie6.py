def reverse_words(text):
    words = text.split()
    reversed_words = [w[::-1] for w in words]
    reversed_text = ' '.join(reversed_words)
    return reversed_text
text = "Ala ma kota"
reversed_text = reverse_words(text)
print(reversed_text) 