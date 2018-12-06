text = 'cbc-training-'
anz_accounts = 15
import string
import secrets
for i in range(1, anz_accounts + 1):
    if i < 10:
     #   prefix = prefix + 1
#    text = text + "0" + str(i)
        print("Accountname: ", text + "0" + str(i))
    else:
        print("Accountname: ", text + str(i))

Password = ''.join(secrets.choice(string.ascii_uppercase
                   + string.digits +
                   string.ascii_lowercase) for _ in range(15))
print(Password)

dic_pass = {"1" : "bla", "2" : "bla2"}
print(dic_pass)
dic_pass.update({"3" : "bla3"})
print(dic_pass)

for key in dic_pass:
    print(key, dic_pass[key])
