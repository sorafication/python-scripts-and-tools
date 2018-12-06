geheimzahl = 1337
versuch = 0
zaehler = 0
while versuch != geheimzahl:
    versuch = int(input("Raten Sie: "))
    if versuch < geheimzahl:
        print("Zahl", versuch, "zu klein")
    if versuch > geheimzahl:
        print("Zahl", versuch, "zu groß")
    zaehler = zaehler + 1
print("Super, Sie haben es nach ", zaehler, "Versuchen geschafft!")
