'''This file is part of a Tkinter course on LinkedIn Learning. It is
intended to test my knowledge of the information presented in the course
by building a simple comment form for an outdoor tours company.
Author: Evan L. Douglass'''

import tkinter as tk
from tkinter import ttk

class CommentForm(ttk.Frame):
    '''Basic comment form for a hypothetical outdoor tour service.'''

    def __init__(self, master):
        '''Sets up all widgets for the app.'''
        self.master = master
        # Heading
        self.logo = tk.PhotoImage(file="C:\\Users\\Evan\\Code\\Python\\TkTutorial\\Images\\tour_logo.gif").subsample(2, 2)
        self.content_title = ttk.Label(master, text="Desert to Sea Tour", 
                                               image=self.logo,
                                               compound='left',
                                               font=('sans-serif', 13),
                                               anchor='center')
        
        # Name                                 
        self.name_label = ttk.Label(master, text="Name")
        self.name_entry = tk.Entry(master, font=('serif', 10))
        
        # Email
        self.email_label = ttk.Label(master, text="Email")
        self.email_entry = tk.Entry(master, font=('serif', 10))

        # Comments (uses text.get for retrieval)
        self.comment_label = ttk.Label(master, text="Comments")
        self.comment_entry = tk.Text(master, height=10, width=50, wrap='word',
                                          font=('serif', 10))

        # Buttons
        self.btn_frm = ttk.Frame(master)
        self.submit = ttk.Button(self.btn_frm, text="Submit", command=self.submit)
        self.cancel = ttk.Button(self.btn_frm, text="Cancel", command=self.clear)

        # Thank you message
        self.thanks_lbl = ttk.Label(master, text="Thank you for your feedback!")

        # Arrange Widgets
        self.grid_all()

        # Configure grid
        self.configure_grid()
    
    def submit(self):
        '''Logs each entry in the form then resets form.'''
        # Get entries
        name = self.name_entry.get()
        email = self.email_entry.get()
        comments = self.comment_entry.get('1.0', 'end')

        # Log/print entries
        print("customer:", name,
               "\nemail:", email,
               "\ncomments:", comments.strip())
        
        # Reset form and disable further entries
        self.clear()

        # Disable further entries
        self.disable()

        # Thank you message
        self.thanks_lbl.grid(row=5, column=0, columnspan=2)

    def clear(self):
        '''Resets form without saving any current information.'''
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.comment_entry.delete('1.0', 'end')

    def disable(self):
        '''Disable entry field areas.'''
        self.name_entry.config(state=tk.DISABLED)
        self.email_entry.config(state=tk.DISABLED)
        # Text default disabled color is different than entry, had to set manually.
        self.comment_entry.config(state=tk.DISABLED, background='#f0f0f0')
        self.submit.config(state=tk.DISABLED)
        self.cancel.config(state=tk.DISABLED)

    def grid_all(self):
        '''Organizes app widgets in the master widget.'''
        self.content_title.grid(row=0, column=0, columnspan=2,
                                padx=5, pady=(0,5), sticky='nesw')
        # Name
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1, sticky='ew')

        # Email
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1, pady=5, sticky='ew')

        # Comment box
        self.comment_label.grid(row=3, column=0)
        self.comment_entry.grid(row=3, column=1, pady=(0, 5), sticky='nesw')

        # Buttons
        self.btn_frm.grid(row=4, column=0, columnspan=2)
        self.submit.pack(side=tk.LEFT)
        self.cancel.pack(side=tk.LEFT)

        # Set focus to name entry
        self.name_entry.focus()

    def configure_grid(self):
        '''Set configuration options for the layout grid.'''
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(3, weight=1)


########## Run Application ##########

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Explore California Touring Company")

    content = ttk.Frame(root, padding=5)
    content.grid(row=0, column=0, sticky='nsew')

    form = CommentForm(content)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
