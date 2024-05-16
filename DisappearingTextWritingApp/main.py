from tkinter import Tk, Text, Label, END
from texteditor import TextEditor

"""class TextEditor:
    def __init__(self,):
        self.timer = 6
        self.has_written = False
        self.benutzereingabe_checken()

        #self.text_feld = text_feld
        #self.timer_label = timer_label


    def benutzereingabe_checken(self, event=None):

        if self.has_written:
            self.timer_zurücksetzen()

        else:
            self.has_written = True
            self.countdown()

    def countdown(self):

        if self.has_written:

            self.timer -= 1
            timer_label.config(text=str(self.timer))

            if self.timer <= 0:
                text_feld.delete(1.0, END)
                self.has_written = False
                self.timer_zurücksetzen()

            tk.after(1000, self.countdown)


    def timer_zurücksetzen(self):
        self.timer = 6
"""



tk = Tk()

tk.title("The Most Dangerous Writing Snake")
tk.geometry("1000x400")

#text_feld = Text(tk, height=8, width=100, highlightthickness=1)
text_label = Label(tk, text="Wenn du aufhörst zu schreiben, verschwindet der Text", font=("Courier", 14), pady=20)
text_label.pack()


#timer_label = Label(tk)

text_editor = TextEditor(window=tk)

text_editor.text_feld.bind("<Key>", text_editor.benutzereingabe_checken)
text_editor.timer_label.config(font=("Courier", 14))

#text_feld.pack()
#timer_label.pack()

# Main Loop

tk.mainloop()
