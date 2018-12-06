import re
f = open("c:/Users/wieczoreko/GitHub/hsnr/regex/Google.html", "r")
html = f.read()
f.close()
it = re.finditer(r"<[a].*href=[\"\'](.*?)[\"\'].*>(.*?)</[a]>", html, re.I)
for m in it:
    print("Name: {}, Link: {}".format(m.group(2), m.group(1)))
