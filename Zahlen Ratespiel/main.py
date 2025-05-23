# Module einfügen
import random

# Variablen für das Spiel
zahlenbereich = int(input("Gib die höchste Zahl mit der du raten willst ein: "))
zufallszahl = random.random()
ungerundet = zufallszahl*zahlenbereich
ergebnis = round(ungerundet)
schleife = True
versuche = round(zahlenbereich/2)

# Schleife für das Ratespiel
while schleife==True:
    print("Du hast noch", versuche, "Versuche verbleibend!")
    guess = int(input("Jetzt rate mal: "))
    print("")

    if versuche==0:
        print("Du hast leider alle Versuche aufgebraucht und das Spiel verloren! D:")
        break

    elif guess==ergebnis:
        print("Du hast richtig geraten! Die Zahl ist ", ergebnis)
        break

    elif guess<ergebnis:
        print("Die gesuchte Zahl ist größer. Versuche es erneut!")
        versuche = versuche - 1

    elif guess>ergebnis:
        print("Die gesuchte Zahl ist kleiner. Versuche es erneut!")
        versuche = versuche - 1

    else:
        print("Kein Plan was du gemacht hast.")

# Variablen für das Scoreboard
highscorename = input("Gebe deinen Namen für die Highscore Liste an: ")
genutzeversuche = round(zahlenbereich/2) - versuche
neuereintrag = f"{highscorename},{genutzeversuche}\n"

# Scoreboard lesen
try:
    with open(f"scoreboard{zahlenbereich}.txt", "r") as f:
        eintraege = f.readlines()
except FileNotFoundError:
    eintraege = []

# Scoreboard Überschrift einfügen
if not eintraege or not eintraege[0].startswith("Name"):
    eintraege.insert(0, "Name | Gebrauchte Versuche\n")

# Scoreboard neuer Eintrag einfügen
eintraege.append(neuereintrag)

# Scoreboard Liste in Überschrift und Einträge unterteilen
überschrift = eintraege[0]
eintraege = eintraege[1:]

# Scoreboard sortieren
eintraege.sort(key=lambda x: int(x.strip().split(",")[1]))

# Scoreboard überschreiben
with open(f"scoreboard{zahlenbereich}.txt", "w") as f:
    f.write(überschrift)
    f.writelines(eintraege)