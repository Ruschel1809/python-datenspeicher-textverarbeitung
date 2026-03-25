#---------------------------------------------------------------
# Dateiname: textverarbeitung.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm liest einen Text aus einer Datei, die Unicode Zeichen enthält
# und speichert den Text in einer Variable. Mittels Regex werden alle
# Wörter die mit Großbuchstaben beginnen aus dem Text gefiltert und in einer
# Liste gespeichert. Die Anzahl der Wörter wird in einem Dictionary aus Wort
# und seiner Anzahl gespeichert. Das Dictionary wird in einer JSON Datei gespeichert
# und ausgelesen. Die ausgelesenen Inhalte werden in der Konsole utf-8 kodiert ausgegeben.
# Autor: Helena Rusch
# Letzte Änderung: 24.06.2025
#---------------------------------------------------------------
import json
import re

def generiere_datei_mit_unicode() -> None:
    unicode_text = "Hello World, Hello Äbla, 世界! 🌍🚀 — Привет мир! — مرحبا بالعالم! — שלום עולם! — हैलो वर्ल्ड!"
    try:
        with open("unicode_file.txt", "w", encoding="utf-8") as text_file:
            text_file.write(unicode_text)
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Speichern der Testdatei: ",e)

def read_text_file() -> str:
    try:
        with open("unicode_file.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Datei noch nicht vorhaden. Bitte führe die Option \"Testdaten generieren\" durch.")
    except IOError as e:
        print("Fehler beim Lesen der Testdaten: ",e)

def filter_nach_uppercase(text:str) -> list[str]:
    reg = r"[A-ZÄÖÜ][a-zäöü]+"
    return re.findall(reg, text)

def speichere_dict_in_json(dictionary:dict[str,int]):
    try:
        with open("json_file.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(dictionary))
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Schreiben der JSON: ",e)

def lese_daten_aus_json() ->dict[str,int]:
    try:
        with open("json_file.json", "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError as e:
        print("Datei nicht vorhanden: ",e)
    except IOError as e:
        print("Fehler beim Laden der Datei: ",e)


generiere_datei_mit_unicode()
woerter = filter_nach_uppercase(read_text_file())
d= {}
for wort in woerter:
    if wort in d:
        d[wort] = d[wort] + 1
    else:
        d[wort] = 1
speichere_dict_in_json(d)
daten = lese_daten_aus_json()
for elem in daten:
    print(f"{elem}: {daten[elem]}")