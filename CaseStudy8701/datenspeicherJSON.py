#---------------------------------------------------------------
# Dateiname: datenspeicherJSON.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm speichert und lädt Daten von und in eine Datei mit JSON-Format
# Autor: Lena
# Letzte Änderung: 19.06.2025
#---------------------------------------------------------------
import json as j

FILE="kontakte.json"

def speichere_kontakt(liste: list[tuple]) -> None:
    existing = []
    try:
        with open(FILE,"r") as f:
            existing = j.load(f)
    except FileNotFoundError:
        pass # Datei gibt es noch nicht, nicht schlimm
    except j.JSONDecodeError as e:
        existing = []
        print("Datei existiert, enthält aber kein gültiges JSON: ", e)
    except IOError as e:
        print("Fehler beim Lesen: ", e)
    for name, email, tel in liste:
        d = {"name" : name.strip(), "email" : email.strip(), "tel" : tel.strip()}
        existing.append(d)

    try:
        with open(FILE,"w") as f:
            j.dump(existing,f, indent = 2)
    except IOError as e:
        print("Fehler beim Schreiben der Datei: ", e)


def lade_kontakte():
    try:
        with open(FILE,"r") as f:
           return j.load(f)
    except FileNotFoundError:
        print("noch keine Kontakte gespeichert.")
    except j.JSONDecodeError as e:
        print("Datei enthält ungültiges JSON: ",e)
    except IOError as e:
        print("Fehler beim Laden: ", e)

def main () -> None:
    print("Adressbuch")
    eingabe = ""
    counter = 0

    while eingabe != "e":
        eingabe = input("[s] Neue Kontakte speichern.\n[l] Vorhandene Kontakte anzeigen.\n[e] Programm beenden.\n").strip()
        if eingabe == "e":
            print("Programm beendet.")
        elif eingabe == "s":
            liste= []
            while True:
                eingabe_zum_speichern = input("Gib Name, E-Mail Adresse, Telefonnummer ein (oder se zum Beenden):\n")
                if eingabe_zum_speichern.lower().strip() == "se":
                    break
                try:
                    name, email, tel = [teil.strip() for teil in eingabe_zum_speichern.split(",")]
                    liste.append((name,email,tel))
                    counter += 1
                except ValueError:
                    print("Ungültige Eingabe. Bitte genau drei Werte mit Komma getrennt eingeben.")
            speichere_kontakt(liste)
            if counter:
                print(f"Es wurden {counter} kontakten gespeichert")
        elif eingabe == "l":
            kontakte = lade_kontakte()
            if kontakte:
                print("Deine Kontakte:")
                for i,k in enumerate(kontakte, 1): # enumerate erzeugt beim Durchlaufen einer Liste ein Tupel aus Index und Wert. Damit die Zählung bei 1 und nicht bei 0 (Standard) beginnt, wird der Start mit angegeben
                    print(f"{i}. {k["name"]} | {k["email"]} | {k["tel"]}")
            else:
                print("Deine Kontakte gespeichert.")

if __name__ == "__main__":
    main()

# Musterlösung
# def speichere_kontakt(name, email, telefon):
#
#     kontakt = {'Name': name, 'E-Mail': email, 'Telefonnummer': telefon}
#     try:
#         with open('kontakte.json', 'r+') as file:
#             daten = json.load(file)
#             daten.append(kontakt)
#             file.seek(0)
#             json.dump(daten, file, indent=4)
#     except (FileNotFoundError, json.JSONDecodeError):
#         with open('kontakte.json', 'w') as file:
#             json.dump([kontakt], file, indent=4)
#         print("Neue Datei wurde erstellt, da keine vorhanden war.")
# def lade_kontakte():
#     try:
#         with open('kontakte.json', 'r') as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         print("Fehler beim Laden der Kontakte. Datei existiert nicht oder ist beschädigt.")
#         return []
# def benutzeroberflaeche():
#     while True:
#         aktion = input("Möchten Sie einen neuen Kontakt speichern (s) oder vorhandene Kontakte anzeigen (a)? (s/a/beenden): ")
#         if aktion.lower() == 'beenden':
#             break
#         elif aktion.lower() == 's':
#             name = input("Name: ")
#             email = input("E-Mail: ")
#             telefon = input("Telefonnummer: ")
#             speichere_kontakt(name, email, telefon)
#             print("Kontakt gespeichert.")
#         elif aktion.lower() == 'a':
#             kontakte = lade_kontakte()
#             if kontakte:
#                 for kontakt in kontakte:
#                     print(f"Name: {kontakt['Name']}, E-Mail: {kontakt['E-Mail']}, Telefonnummer: {kontakt['Telefonnummer']}")
#             else:
#                 print("Keine Kontakte gefunden.")
#         else:
#             print("Ungültige Eingabe.")
# if __name__ == "__main__":
#     benutzeroberflaeche()