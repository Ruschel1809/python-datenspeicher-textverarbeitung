#---------------------------------------------------------------
# Dateiname: textverarbeitung.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet verschiedene String-Methoden, um Text zu verarbeiten
# Autor: Lena
# Letzte Änderung: 23.06.2025
#---------------------------------------------------------------
import json

text="""
das ist ein mehrzeiliger Text, der als Unicode-Zeichen ein Emoji enthält: \U0001F600 
Weiterhin enthält es eine Escape-Sequenz \n die einen Zeilenumbruch angibt.der variable Teil ist {0} obwohl das im Skript mal wieder kein Thema war :("""
#print(text.format("variable Teile"))

def speichere_text_in_datei(s:str) -> None:
    try:
        with open("beispieltext.txt","w", encoding="utf-8") as f:
            f.write(s)
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Speichern: ", e)

def lese_text_aus_datei() -> str | None:
    try:
        with open("beispieltext.txt","r", encoding="utf-8") as f:
           return f.read()

    except FileNotFoundError:
        print("Noch keine Datei gespeichert.")
    except IOError as e:
        print("Fehler beim Lesen: ", e)
    return None

def speichere_json(d:dict) -> None:
    try:
        with open("beispieltext.json","w", encoding="utf-8") as f:
            json.dump(d,f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        pass
    except IOError as e:
        print("Fehler beim Speichern der JSON-Datei: ", e)

speichere_text_in_datei(text)
t = lese_text_aus_datei()
print(t)

woerterbuch = {1 : "a", 2: "b", 3: "c", 4: "d"}
speichere_json(woerterbuch)
