#---------------------------------------------------------------
# Dateiname: datenSpeicher.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm speichert und lädt Daten
# Autor: Lena
# Letzte Änderung: 18.06.2025
#---------------------------------------------------------------



def speichere_daten(l:list[tuple]):
    try:
        with open("personen.txt","w") as f:
            for elem in l:
                n,a = elem
                f.write(str(n) + " : " + str(a) + "\n")
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except PermissionError:
        print("Zugriff auf Datei verweigert")
    except Exception as e:
        print("Es ist ein unbekannter Fehler aufgetreten", e)

def lade_daten() -> list[dict[str, str]]:
    liste_von_dicts = []
    try:
        with open("personen.txt","r") as f:
            for line in f:
                d = {"name":line.split(":")[0], "alter": line.split(":")[1]}
                liste_von_dicts.append(d)
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except PermissionError:
        print("Zugriff auf Datei verweigert")
    except Exception as e:
        print("Es ist ein unbekannter Fehler aufgetreten", e)
    finally:
        return liste_von_dicts


speichere_daten([("Klaus", "13"), ("Anna", "24")])
geladene_daten = lade_daten()
if geladene_daten:
    for l in geladene_daten:
        print(f"Name: {l['name']}, Alter: {l['alter']}")
else:
    print("Hat nicht geklappt")
