def binaere_suche(arr, ziel):
    # Start und Ende des Bereichs festlegen
    links = 0
    rechts = len(arr) - 1

    while links <= rechts:
        # Divide: Mittleren Index berechnen
        mitte = (links + rechts) // 2

        # Conquer: Prüfen, ob das Ziel am mittleren Index liegt
        if arr[mitte] == ziel:
            return mitte  # Ziel gefunden, Index zurückgeben

        # Conquer: Wenn das Ziel größer ist, suche im rechten Teil weiter
        elif arr[mitte] < ziel:
            links = mitte + 1

        # Conquer: Wenn das Ziel kleiner ist, suche im linken Teil weiter
        else:
            rechts = mitte - 1

    # Merge: Ziel nicht gefunden, -1 zurückgeben
    return -1


# Beispiel-Liste (muss sortiert sein)
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Zielwert, den wir suchen möchten
zielwert = 17

# Binäre Suche ausführen
ergebnis = binaere_suche(array, zielwert)

# Ergebnis ausgeben
if ergebnis != -1:
    print(f"Zielwert {zielwert} gefunden an Index {ergebnis}.")
else:
    print(f"Zielwert {zielwert} nicht in der Liste gefunden.")
