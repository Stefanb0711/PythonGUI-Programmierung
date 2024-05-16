from tkinter import Tk, Text, Label, END


class TextEditor:
    def __init__(self, window):
        self.tk = window
        self.timer = 6
        self.has_written = False
        #self.benutzereingabe_checken()

        """self.text_feld = text_feld
        self.timer_label = timer_label
        self.tk = window"""

        self.text_feld = Text(self.tk, height=8, width=100, highlightthickness=1)
        self.timer_label = Label(self.tk)
        self.text_feld.pack()
        self.timer_label.pack()


    def benutzereingabe_checken(self, event=None):

        if self.has_written:
            self.timer_zurücksetzen()

        else:
            self.has_written = True
            self.countdown()

    def countdown(self):

        if self.has_written:

            self.timer -= 1
            self.timer_label.config(text=str(self.timer))

            if self.timer <= 0:
                self.text_feld.delete(1.0, END)
                self.has_written = False
                self.timer_zurücksetzen()

            self.tk.after(1000, self.countdown)


    def timer_zurücksetzen(self):
        self.timer = 6
