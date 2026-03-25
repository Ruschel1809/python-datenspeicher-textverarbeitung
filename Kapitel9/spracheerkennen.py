#---------------------------------------------------------------
# Dateiname: glueckskeks.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm erkennt die Sprache eines eingegebenen Textes aus 
# mindestens 50 Zeichen.
# Es kann zwischen Deutsch, Englisch unterscheiden. 
#---------------------------------------------------------------
# Autor: Lena
# Letzte Änderung: 24.06.2025
#---------------------------------------------------------------
import re

def sprache_erkennen(text):
    # Überprüfen, ob der Text mindestens 50 Zeichen lang ist
    if len(text) < 50:
        return "Der Text muss mindestens 50 Zeichen lang sein."

    # Regex-Muster für deutsche und englische Wörter
    deutsch_muster = r'\b(der|die|das|und|zu|von|mit|auf|für|ist)\b'
    englisch_muster = r'\b(the|and|out|to|of|with|on|for|is)\b'

    # Zählen der Vorkommen der Muster im Text
    deutsch_count = len(re.findall(deutsch_muster, text, re.IGNORECASE))
    englisch_count = len(re.findall(englisch_muster, text, re.IGNORECASE))


    # Bestimmen der Sprache
    if deutsch_count > englisch_count:
        return "Es wurden {} deutsche Wörter und {} englische Wörter gefunden.\nDer Text ist wahrscheinlich auf Deutsch.".format(deutsch_count, englisch_count)
    elif englisch_count > deutsch_count:
        return "Es wurden {} englische Wörter und {} deutsche Wörter gefunden.\nDer Text ist wahrscheinlich auf Englisch.".format(englisch_count, deutsch_count)
    else:
        return "Die Sprache des Textes kann nicht eindeutig bestimmt werden."   
# Hauptprogramm
if __name__ == "__main__":
    text = input("Bitte geben Sie einen Text mit mindestens 50 Zeichen ein:\n")
    ergebnis = sprache_erkennen(text)
    print(ergebnis)