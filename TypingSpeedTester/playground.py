import time
from tkinter import *


window = Tk()

textfeld = Text(window, wrap="word", width=40, height=20, pady=20)
textfeld.pack()

def ergebniss_zeigen():

    print(int(len(textfeld.get("1.0", "end-1c")) / 4))
    #print(int(len(textfeld.get()) / 4))


button = Button(window, text="Start", command= ergebniss_zeigen)
button.pack()

window.mainloop()