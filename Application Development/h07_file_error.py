#h07_file_error.py
filenames=['anna.txt','gatsby.txt','don_quixote.txt','beloved.txt','mockingbird.txt']


for i in filenames:
    try:
        file= open(i, 'r+',encoding='utf8')
        read=file.read()
        words= read.split()
        num= len(words)
        print("This file:", i, "has", num, "words")
    except FileNotFoundError:
        print("File:", i, "does not exist")