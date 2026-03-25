#---------------------------------------------------------------
# Dateiname: newsCheck.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm durchsucht die Seite https://www1.wdr.de/index.html nach Nutzerschlagworten
# Autor: Lena
# Letzte Änderung: 18.06.2025
#---------------------------------------------------------------

from urllib.request import urlopen

url = "https://www1.wdr.de/index.html"
def lesen():
    with urlopen(url) as response:
        rohdaten = response.read()
    text = rohdaten.decode()
    return text
    # print()
    # print(text)
    # print()

schlagwort = "a"
while schlagwort != "":
    print("Schlagwort Suche auf der Startseite der WDR")
    schlagwort = input("Schlagwort: ")
    seite = lesen()
    if schlagwort == "":
        break
    elif schlagwort != "" and schlagwort in seite:
        print(f"{schlagwort} kommt auf der Startseite des WDR vor.")
    else:
        print(f"{schlagwort} kommt auf der Startseite des WDR nicht vor.")