#---------------------------------------------------------------
# Dateiname: glueckskeks.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm gibt zufällige Glückskeks-Texte aus. Ein 
# Glückskekstext setzt sich aus zwei Teilen zusammen: 
# Erster Teil: eine Aufforderung z.B. Achte
# Zweiter Teil: ein positiv belegtes Objekt z.B. das Leben
# Der zusammengesetzte Text wird dann in der Konsole ausgegeben.
#---------------------------------------------------------------
# Autor: Lena
# Letzte Änderung: 24.06.2025
#---------------------------------------------------------------
import random

def glueckskeks():
    # Listen mit Textteilen
    aufforderungen = [
        "Achte",
        "Genieße",
        "Vertraue",
        "Lerne",
        "Entdecke"
    ]
    
    objekte = [
        "das Leben",
        "die Liebe",
        "deine Freunde",
        "die Natur",
        "deine Träume"
    ]
    
    # Zufällige Auswahl eines Teils aus jeder Liste
    teil1 = random.choice(aufforderungen)
    teil2 = random.choice(objekte)
    
    # Zusammensetzen des Glückskeks-Texts
    glueckskeks_text = f"{teil1} {teil2}!"
    
    return glueckskeks_text

# Hauptprogramm
if __name__ == "__main__":
    print("Dein Glückskeks-Spruch:")
    print(glueckskeks())