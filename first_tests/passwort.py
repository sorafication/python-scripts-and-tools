import hashlib
pwhash = hashlib.md5(b"Passwort")
pwinput = input("Geben Sie ihr Passwort ein: ")
print("Ihr Passwort lautet: ", pwinput)
print("MD5 des Passwortes lautet: ", pwhash.hexdigest())
pwinputhash = hashlib.md5(pwinput.encode('utf-8')).hexdigest()
print("MD5 Ihres Passwortes: ", pwinputhash)
if pwhash.hexdigest() == pwinputhash:
    print("Glueck Gehabt ;)")
else:
    print("Du kommst hier nich rein")
