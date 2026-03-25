import json
freunde = ["Anna Aa", "Bobo Be", "Cora Ce", "Dora De", "Emil Ee"]
try:
    with open("freunde.txt", "w") as file:
        json.dump(freunde, file)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Speichern der Liste: {e}")

try:
    with open("freunde.txt", "r") as file:
        geladene_liste = json.load(file)
        print("Geladene Freunde Liste:", geladene_liste)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Laden der Liste: {e}")

try:
    with open("freunde.txt", "r+") as file:
        freunde_liste = json.load(file)
        freunde_liste.append("Felix")  # Neuen Namen hinzufügen
        file.seek(0)  # Zurück zum Anfang der Datei gehen
        json.dump(freunde_liste, file)
        file.truncate()  # Entfernt überschüssige Daten am Ende der Datei
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Aktualisieren der Liste: {e}")