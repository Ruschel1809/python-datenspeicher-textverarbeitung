#---------------------------------------------------------------
# Dateiname: textverarbeitung.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet verschiedene String-Methoden, um Text zu verarbeiten
# Autor: Lena
# Letzte Änderung: 23.06.2025
#---------------------------------------------------------------
# Meins angefangen
# def lese_text_aus_datei() -> str | None:
#     try:
#         with open("tagebuch.txt","r", encoding="utf-8") as f:
#            return f.read()
#
#     except FileNotFoundError:
#         print("Noch keine Datei gespeichert.")
#     except IOError as e:
#         print("Fehler beim Lesen: ", e)
#     return None
#
# alter_text = lese_text_aus_datei().lower()
# wortliste = alter_text.split()

#Musterlösung
import json


def zaehle_wort(text, wort):
    return text.lower().count(wort.lower())


def ersetze_wort(text, alt, neu):
    return text.replace(alt, neu)


def teile_in_saetze(text):
    return text.split('.')


def speichere_als_json(dateiname, daten):
    with open(dateiname, 'w', encoding='utf-8') as file:
        json.dump(daten, file, ensure_ascii=False, indent=4)


try:
    with open('tagebuch.txt', 'r', encoding='utf-8') as file:
        inhalt = file.read()
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
else:
    wort_vorkommen = zaehle_wort(inhalt, 'traurig')
    print(f"Das Wort 'traurig' kommt {wort_vorkommen} Mal vor.")

    aktualisierter_text = ersetze_wort(inhalt, 'traurig', 'glücklich')

    with open('tagebuch_neu.txt', 'w', encoding='utf-8') as neue_datei:
        neue_datei.write(aktualisierter_text)

    saetze = teile_in_saetze(aktualisierter_text)
    speichere_als_json('tagebuch_saetze.json', saetze)
