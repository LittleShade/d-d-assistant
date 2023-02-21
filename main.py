import tkinter as tk
from tkinter import ttk
import os
import campaign_searcher as cs
import campaign_creation as cc

# root window
root = tk.Tk()
root.title('Tabletop Assistant')
root.geometry('150x70')


# frame
frame = ttk.Frame(root)


frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#create button function

def create_button_clicked():
    """  Handle create button click event 
    """
    cc.create()

#create button set up

convert_button = ttk.Button(frame, text='Create new campaign')
convert_button.grid(column=0,row=0)
convert_button.configure(command=create_button_clicked)

#open button function

def open_button_clicked():
    """  Handle open button click event 
    """
    cs.searchmenu()

#open button set up

convert_button = ttk.Button(frame, text='open campaign')
convert_button.grid(row=1)
convert_button.configure(command=open_button_clicked)


# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()
