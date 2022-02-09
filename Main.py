from sympy import *
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from Button import InputButton
from sympy import symbols
from sympy.plotting import plot
from Graf import GrafClass
import matplotlib




class mainWindowClass:
    def __init__(self):
        self.target = 4500
        self.root = Tk()


        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        #PressButton = Button(self.root, text="Liste over indbetalinger", command=lambda: listWindowClass(self))
        #PressButton.pack(padx=20, pady=10, side=LEFT)

        Buttonpress = Button(self.root, text="Graf Input", command=lambda: InputButton(self))
        Buttonpress.pack(padx=20, pady=10, side=LEFT)

        mainloop()

if __name__ == '__main__':
    main = mainWindowClass()
