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

	x = float(plot_Input.get())

	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),
				dpi = 100)

	# list of squares
	#
	y = [i**x for i in range(101)]

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y,c = HexC)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,
							master = window)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,
								window)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

# button that displays the plot
plot_button = Button(master = window,
					command = plot,
					text = "Plot")

plot_Input = Entry()

variable = StringVar(window)
variable.set("i**x")


plot_tab = OptionMenu(window, variable, "i**x", "two", "three")
plot_label = Label(window, text = "skriv værdien for x")

# place the button
# in main window
plot_tab.pack(pady = 5, side=tk.TOP)
plot_label.pack()
plot_Input.pack(pady = 5, side=tk.TOP)
plot_button.pack(pady = 5, side=tk.TOP)


# run the gui
window.mainloop()
