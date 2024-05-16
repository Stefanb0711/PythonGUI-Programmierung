from tkinter import *
from tkinter import filedialog
import pyttsx3
from gtts import gTTS
import os



window = Tk()
window.geometry("600x400")
window.resizable(False, False)


text_to_speak = ""

def save_file():
    global text_to_speak

    text_to_speak = text_feld.get("1.0", END)

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Textdateien", "*.mp3"), ("Alle Dateien", "*.*")])

    if file_path:
        engine = pyttsx3.init()
        engine.save_to_file(text_to_speak, filename=file_path)
        engine.runAndWait()
        os.system(f"start {file_path}")



def play_audiobook():

    text_to_speak = text_feld.get("1.0", END)


    engine = pyttsx3.init()

    engine.say(text_to_speak)
    engine.runAndWait()


menubar = Menu(window)
window.config(menu = menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Datei", menu=file_menu)

file_menu.add_command(label="Neu")

file_menu.add_command(label="Speichern unter", command=save_file)




text_label = Label(window, text="Der zu konvertierende Text: ", font=("Courier"), pady=20)
text_label.pack()


text_feld = Text(window, width=40, height=10)
text_feld.pack()

button_play = Button(window, text="Play",command=play_audiobook)
button_play.pack(pady = 30)



user_input = ""



def get_user_input(event):
    global user_input


    user_input = text_feld.get("1.0", END)
    print(user_input)


#text_to_speak = text_feld.get()
text_feld.bind("<Key>", get_user_input)


#text_feld = Text(window, width=)

"""# Text, den Sie in Sprache umwandeln möchten
text_to_speak = "Hallo, wie geht es Ihnen?"

# Erstellen Sie ein gTTS-Objekt
tts = gTTS(text=text_to_speak, lang='de')

# Speichern Sie die Sprachdatei als Audio-Datei
tts.save("output.mp3")

# Optional: Direkt abspielen (benötigt ein Audiowiedergabe-Tool)
os.system("start output.mp3")
"""

window.mainloop()
