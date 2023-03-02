#Zadanie1
input_str = input("Podaj dane oddzielone separatorem: ")
source_sep = input("Podaj separator źródłowy: ")
target_sep = input("Podaj separator docelowy: ")

data_list = input_str.split(source_sep)
output_str = target_sep.join(data_list)

print("Wynik: ", output_str)

#Zadanie2
lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#Zadanie3
imie = "Wiktoria"
litera_1 = imie[2]
nazwisko = "Gawrońska"
litera_2 = nazwisko[3]
liczba_liter1 = lorem_ipsum.count(litera_1)
liczba_liter2 = lorem_ipsum.count(litera_2)
print("W tekście jest '{}' liter '{}' oraz '{}' liter '{}'".format(liczba_liter1, litera_1, liczba_liter2, litera_2))