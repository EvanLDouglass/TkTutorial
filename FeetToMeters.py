from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

def calculate(*args):
    '''Converts feet to meters'''
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Main application frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
# Allow frame to resize with window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()
# Where the user types in a number in feet
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
# Where the resulting meters are displayed
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
# The button to activate the application
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, stick=W)

# The permanent text in the window
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Add padding to all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# Set focus on text entry field
feet_entry.focus()
# Allow user to also press Enter to activate calculation
root.bind('<Return>', calculate)

root.mainloop()
