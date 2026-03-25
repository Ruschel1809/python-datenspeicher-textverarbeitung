#---------------------------------------------------------------
# Dateiname: sonderzeichen_unicode.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm sucht und ersetzt Wörter in einem String
# Autor: Helena Rusch
# Letzte Änderung: 25.06.2025
#---------------------------------------------------------------
import json as j

text="""Ähhh ein \"Text\"\n
        mit Unicode\n \t \u2764 und \U0001F600\n
        und ein bisschen Sprachen Привет мир!"""

def wort_ersetzen(altw:str, neuw:str):
    mod_text = text.replace(altw,neuw)
    print(mod_text)
    speichere_text(mod_text)

def speichere_text(t:str):
    with open("modifizierter_text.txt", "w", encoding="utf-8") as f:
        f.write(t)
def lies_json():

    with open("daten.json", "r", encoding="utf-8") as f:
        return j.loads(f.read())

eingabe = input("Welches Wort wird gesucht: ")
erg = text.count(eingabe)
print(f"{eingabe} wurde {erg} Mal gefunden.")
ersatz = input(f"Durch welches Wort soll {eingabe} ersetzt werden: ")
wort_ersetzen(eingabe, ersatz)
lies_json()

