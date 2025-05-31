import sys

sys.stdout.reconfigure(encoding='utf-8')

def mymax(iterable, key=lambda x: x):
    # Inicijalizacija maksimalnog elementa i maksimalnog ključa
    max_x = max_key = None

    # Obiđi sve elemente
    for x in iterable:
        # Ako je key(x) najveći, ažuriraj max_x i max_key
        if max_x is None or key(x) > max_key:
            max_x = x
            max_key = key(x)

    # Vrati rezultat
    return max_x

words = ["Gle", "malu", "vocku", "poslije", "kise", "Puna", "je", "kapi", "pa", "ih", "njise"]
print(mymax(words, key=lambda x: len(x)))

maxint = mymax([1, 3, 5, 7, 4, 6, 9, 2, 0]) # default; key = element

print(maxint)

D = {'burek': 8, 'buhtla': 5}
print(mymax(D, key = D.get)) 

people = [("Marko", "Marulić"), ("Marko", "Markotić"), ("Marko", "Šijak")]
print(mymax(people))

maxchar = mymax("Suncana strana ulice")
maxstring = mymax(words)

print(maxchar)
print(maxstring)