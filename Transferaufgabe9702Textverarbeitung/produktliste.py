#---------------------------------------------------------------
# Dateiname: produktliste.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm pflegt eine Produktliste und berechnet die MwSt
# Autor: Helena Rusch
# Letzte Änderung: 25.06.2025
#---------------------------------------------------------------
import re


def ergaenze_preis_mit_steuer(produktliste: list, steuersatz: float = 19) -> list[tuple[str,float,float]]:
    """
    Berechnet den Preis inklusive Steuern.

    :param produktliste: Liste mit Tupeln aus Produkt und Preis
    :param steuersatz: Steuersatz in Prozent

    :return: Liste mit Tupeln aus Produkt, Preis, Preis mit MwSt
    """
    produkte_mit_mwst=[]
    for elem in produktliste:
        produkt,preis = elem
        neuer_preis = preis * (1 + steuersatz / 100)
        t=(produkt,preis,round(neuer_preis,2))
        produkte_mit_mwst.append(t)
    return produkte_mit_mwst

# produkte_ohne_mwst = [("Milch",1.29),("Brot",2.5),("Äpfel",3.19)]
# with open("produkte_ohne_MwSt.txt", "w", encoding="utf-8") as f:
#     for produkt in produkte_ohne_mwst:
#         f.write(produkt[0] + "," + str(produkt[1]) + "\n")

produkte_ohne_mwst = []
# reg = r"\w+ *\w" # macht dasgleiche wie unten unt unterstrich wird auch akzeptiert
reg= r"[a-zA-Z0-9äöüÄÖÜß]+ *[a-zA-Z0-9äöüÄÖÜß]*"
try:
    with open('produkte_ohne_MwSt.txt', 'r', encoding="utf-8") as f:
        inhalt=f.read()
except FileNotFoundError as e:
    print("Die Datei ist nicht vorhanden: ", e )
except IOError as e:
    print("Fehler beim Lesen der Datei: ", e)
else:
    produkte = inhalt.split("\n")
    print(produkte)
    for elem in produkte:
        if elem != "":
            if re.match(reg, elem[0]):
                produkt,preis = elem.split(",")
            else:
                continue
            try:
                t=(produkt,float(preis))
                produkte_ohne_mwst.append(t)
            except ValueError:
                print(f"der Preis für {produkt} hat keinen gültigen Wert. {preis}")
                continue
    print(produkte_ohne_mwst)

with open("produkte_mit_MwSt.txt", "w", encoding="utf-8") as f:
     for produkt in ergaenze_preis_mit_steuer(produkte_ohne_mwst):
         f.write(produkt[0] + "," + str(produkt[1]) + "," + str(produkt[2]) + "\n")