#---------------------------------------------------------------
# Dateiname: speichernUndladen.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm speichert und lädt Daten
# Autor: Lena
# Letzte Änderung: 18.06.2025
#---------------------------------------------------------------

def speichere_daten(liste: list[tuple]) -> None:
    try:
        with open("studentendaten.txt","w") as f:
            for elem in liste:
                n, m, s = elem
                f.write(f'Name: {n} , Matrikelnummer: {m}, Studiengang: {s}\n')
    except IOError as e:
        print("Fehler: ",e)

def lade_daten() -> list[dict[str, str]]:
    liste_von_dicts = []
    try:
        with open("studentendaten.txt","r") as f:
            for line in f:
                d = {"name":line.split(",")[0].split(":")[1], "matrikel": line.split(",")[1].split(":")[1], "studium": line.split(",")[2].split(":")[1]}
                liste_von_dicts.append(d)
    except IOError as e:
        print("Fehler: ", e)
    finally:
        return liste_von_dicts



speichere_daten([("Klaus", "13567","Mathe"), ("Anna", "24453", "Info")])
geladene_daten = lade_daten()
if geladene_daten:
    for l in geladene_daten:
        print(f"Name: {l['name']}, Matrikelnummer: {l['matrikel']}, Studiengang: {l['studium']}")
else:
    print("Hat nicht geklappt")