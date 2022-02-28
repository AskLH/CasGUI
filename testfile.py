from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

# plot function is created for
# plotting the graph in
# tkinter window



def plot():

	x = float(plot_Input.get())

	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),
				dpi = 100)

	# list of squares
	y = [i**x for i in range(101)]

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y)

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
					height = 2,
					width = 10,
					text = "Plot")

plot_Input = Entry()

variable = StringVar(window)
variable.set("i**x")


plot_tab = OptionMenu(window, variable, "i**x", "two", "three")
plot_label = Label(window,"skrive værdien for x")

# place the button
# in main window
plot_tab.pack()
plot_button.pack()
plot_Input.pack()
plot_label.pack()

# run the gui
window.mainloop()
