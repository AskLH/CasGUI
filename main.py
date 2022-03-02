import tkinter as tk
import random
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


# plot function is created for
# plotting the graph in
# tkinter window

colors = random.randint(0,16777215)
HexC= hex(colors)
HexC= '#'+ HexC[2:]
print(HexC)

def plot():

	x = float(plot_Input.get()) #variabel til brugerinput

	# her bliver størrelsen og opløsningen af grafen defineret
	fig = Figure(figsize = (5, 5),
				dpi = 100)


	y = [i**x for i in range(101)] #Funktionen for grafen

	plot1 = fig.add_subplot(111) #

	# plotting the graph
	plot1.plot(y,c = HexC) #her tegnes grafen med den random generede farve

	#Her laves tk canvasset med matplotlibfigure
	canvas = FigureCanvasTkAgg(fig,
							master = window)
	canvas.draw()

	#Vinduet laves
	canvas.get_tk_widget().pack()

#vi skaber et vindue
window = Tk()

window.title('Plotting in Tkinter')

window.geometry("500x500")

#der laves en knap til at plotte grafen
plot_button = Button(master = window,
					command = plot,
					text = "Plot")

plot_Input = Entry() #en funktion der tager mod bruger input i vinduet

#der laves en dropdown menu med funktionen variabler
variable = StringVar(window)
variable.set("i**x")
#vi skaber menu
plot_tab = OptionMenu(window, variable, "i**x", "two", "three")
plot_label = Label(window, text = "skriv værdien for x")

#knappen, inputtet, dropdownmenuen og et label bliver plottet ind i vinduet
plot_tab.pack(pady = 5, side=tk.TOP)
plot_label.pack()
plot_Input.pack(pady = 5, side=tk.TOP)
plot_button.pack(pady = 5, side=tk.TOP)



window.mainloop()
