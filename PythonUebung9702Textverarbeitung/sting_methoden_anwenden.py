import json

text_als_string=f"das ist ein Text mit einem Omega, das sieht so aus\n {chr(int("03A9",base=16))}"
text_als_string +="\noh mannsen"

anzahl=text_als_string.count("a")
print(anzahl," As im text")
liste_mit_strings=["a","b","c","d","e","f"]
neuer_string=",".join(liste_mit_strings)

with open("bla.txt", "w", encoding="utf-8") as f:
    f.write(text_als_string)

try:
    with open("bla.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Datei nicht vorhanden")
except IOError as e:
    print("Fehler beim lesen der Datei: ",e)

d={1:"Das",2:"ist",3:"ein",4:"weiteres",5:"sinnloses",6:"Dictionary", 7:"für", 8:"sinnloses", 9:"JSON"}
with open("sinnlos.json", "w", encoding="utf-8") as f:
    json.dump(d,f)
with open("sinnlos.json", "r", encoding="utf-8") as f:
    print(f.read())