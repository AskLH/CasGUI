from sympy import *
from tkinter import *
from tkinter.ttk import *



class mainWindowClass:
    def __init__(self):
        self.target = 4500
        # creating tkinter window
        self.root = Tk()

        # TEXT

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        PressButton = Button(self.root, text="Liste over indbetalinger", command=lambda: listWindowClass(self))
        PressButton.pack(padx=20, pady=10, side=LEFT)

        mainloop()

if __name__ == '__main__':
    main = mainWindowClass()

