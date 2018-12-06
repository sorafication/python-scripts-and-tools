fobj = open("c:/Users/wieczoreko/GitHub/hsnr/python_test/woerterbuch.txt", "r")
woerter = {}
for line in fobj:
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]

wort = "anfang"
while True:
    wort = input("Geben Sie das Wort an oder 'ende' zum abbrechen: ")
    if wort in woerter:
        print(woerter[wort])
    elif wort == "ende":
        break
    else:
        print("Das Wort ist unbekannt")
fobj.close()

fobj2 = open("c:/Users/wieczoreko/GitHub/hsnr/python_test/write.txt", "w")
print("Zeit zum reinschreiben: Falls nein 'ende' eintippen")
while True:
    wort2 = input("Geben Sie das neue ein ")
    if wort2 == "ende":
        break
    else:
        fobj2.write(wort)
fobj2.close()
