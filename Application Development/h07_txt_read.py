#h07_txt_read.py


fileobject= open("anna.txt", "r",encoding="utf8")
print(fileobject)

content= fileobject.read()
print(content)