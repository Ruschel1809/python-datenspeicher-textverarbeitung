#---------------------------------------------------------------
# Dateiname: textverarbeitung.py
#---------------------------------------------------------------
# Beschreibung:
# Das Programm verwendet verschiedene String-Methoden, um Text zu verarbeiten
# Autor: Lena
# Letzte Änderung: 23.06.2025
#---------------------------------------------------------------
# angefangen
 def lese_text_aus_datei() -> str | None:
     try:
         with open("tagebuch.txt","r", encoding="utf-8") as f:
            return f.read()

     except FileNotFoundError:
         print("Noch keine Datei gespeichert.")
     except IOError as e:
         print("Fehler beim Lesen: ", e)
     return None

 alter_text = lese_text_aus_datei().lower()
 wortliste = alter_text.split()
