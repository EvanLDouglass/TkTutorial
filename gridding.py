from tkinter import *
from tkinter import ttk

root = Tk()

# Main content frame
content = ttk.Frame(root, padding=(3,3,12,12))
# Frame for a checkbox label
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
onelbl = ttk.Label(frame, text="Current value of checkbox one:", anchor='s')
onevalue = ttk.Label(frame, text="1", anchor='n')  # Will have opposite value than expected
onelbl['background'] = 'red'
onevalue['background'] = 'red'
# Name entry box
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

# Checkbox variables
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

# Make the checkboxes
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=False, offvalue=True, command=lambda: onevalue.config(text=onevar.get()))
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# Buttons
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# Place items in window with grid
content.grid(column=0, row=0, sticky='nsew')
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky='nsew')
onelbl.grid(column=0, row=0, sticky='nesw')
onevalue.grid(column=0, row=1, sticky='nesw')
namelbl.grid(column=3, row=0, columnspan=2, sticky='nw', padx=5)
name.grid(column=3, row=1, columnspan=2, sticky='new', padx=5, pady=5)
one.grid(column=0, row=2)
two.grid(column=1, row=2)
three.grid(column=2, row=2)
ok.grid(column=3, row=2)
cancel.grid(column=4, row=2)

# Configure resizing options
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()