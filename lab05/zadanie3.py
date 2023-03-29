text = 'Ala ma kota.'

result = [(word, [ord(char) for char in word]) for word in text.split()]
print(result)