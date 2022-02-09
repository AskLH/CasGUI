# importing tkinter module
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


class InputButton:

    def __init__(self, master):
        self.master = master
        self.InputButton = Toplevel(self.master.root)
        self.InputButton.title("Pay Window")
        self.InputButton.geometry("200x200")

        Label(self.InputButton,
              text="Graf ligning").pack()

        self.money = Entry(self.InputButton)
        self.money.pack()

        self.button = Button(self.InputButton, text="Tegn", command= self.addMoney)
        self.button.pack()

    def addMoney(self):
        try:
            amount = abs(int(self.money.get()))
        except:
            messagebox.showerror(parent=self.InputButton, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return


        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        self.InputButton.destroy()
