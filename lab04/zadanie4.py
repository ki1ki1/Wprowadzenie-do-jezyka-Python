import this

sentence = input("Podaj zdanie: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
rot13 = alphabet[13:] + alphabet[:13]
rot13_dict = dict(zip(alphabet, rot13))
rot13_dict.update(zip(alphabet.upper(), rot13.upper()))

encoded_sentence = "".join(rot13_dict.get(char, char) for char in sentence)
print(f"Zakodowane zdanie: {encoded_sentence}")