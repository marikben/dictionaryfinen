from tkinter import *
from PyDictionary import PyDictionary
import urllib, json, random

root = Tk()
mainframe = Frame(root)
mainframe.pack()

frame1 = Frame(root)
frame1.pack(side=LEFT,padx=20, pady=20)

frame2 = Frame(root)
frame2.pack(side=RIGHT,padx=20, pady=20)

def getWords():
    for i in range(50):
        n = random.randint(0,len(words))
        word = words[n]
        pairs[0].append(word)
        engbox.insert(i,word)
        
    dictionary = PyDictionary()

    for i in range(len(pairs[0])):
        word = pairs[0][i]
        translation = dictionary.translate(word,'fi')
        pairs[1].append(translation)
        finbox.insert(i, translation)
        
heading = Label(text="FIN-ENG Dictionary")
heading.pack(side=TOP, anchor= CENTER,padx=20, pady=20)
btn = Button(text="Get new words", command=getWords)
btn.pack(side=BOTTOM, anchor= CENTER,padx=10, pady=40)

url = "https://www.randomlists.com/data/words.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
data = json.dumps(data)
data = json.loads(data)
words = data["data"]
pairs = [[],[]]

scrollbar1 = Scrollbar(frame1, orient=VERTICAL)
scrollbar2 = Scrollbar(frame2, orient=VERTICAL)
engbox = Listbox(frame1, yscrollcommand=scrollbar1.set,bg='white')
finbox = Listbox(frame2, yscrollcommand=scrollbar2.set,bg='white')
scrollbar1.config(command=engbox.yview)
scrollbar1.pack(side=RIGHT, fill=Y)
engbox.pack(side=LEFT,anchor=W, fill=BOTH, expand=1, pady=10)
scrollbar2.config(command=finbox.yview)
scrollbar2.pack(side=RIGHT, fill=Y)
finbox.pack(side=TOP,anchor=E,fill=BOTH, expand=1, pady=10)

root.mainloop()
