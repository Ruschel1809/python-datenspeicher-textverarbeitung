import json as j

alter = 5
hobbies = ["lesen", "reiten", "joggen"]
lieblingsfarben = ("rot", "grün", "blau")
FILE = "persoenliche_daten.json"

for hobby in hobbies:
    print(f"Eines meiner Hobbies ist: {hobby}")

def jahre_bis_rente(alter: int) -> int:
    return 65 - alter

def to_json(h: list, l: tuple) -> dict:
    hld={"hobbies":h, "lieblingsfarben":l}
    return hld

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

try:
    with open(FILE,"w", encoding="utf-8") as f:
        j.dump(to_json(hobbies, lieblingsfarben),f, ensure_ascii=False,  indent = 2)
except IOError as e:
    print("Fehler beim Schreiben der Datei: ", e)
