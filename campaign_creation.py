import os
import tkinter as tk
from tkinter import ttk

# root window

def create():

    root = tk.Tk()
    root.title('New campaign')
    root.geometry('300x70')
    root.resizable(False, False)


    # frame
    frame = ttk.Frame(root)


    # field options
    options = {'padx': 5, 'pady': 5}

    # campaign label
    campaign_label = ttk.Label(frame, text='campaign name')
    campaign_label.grid(column=0, row=0, sticky='W', **options)

    # name entry
    campaign = tk.StringVar()
    campaign_entry = ttk.Entry(frame, textvariable=campaign)
    campaign_entry.grid(column=1, row=0, **options)
    campaign_entry.focus()

    # convert button


    def add_button_clicked():
        """  Handle add button click event 
        """
        name=campaign_entry.get()
        if name=="":
            print("error")
        else:
            pos=os.getcwd()
            newDir = pos + "\\campaigns\\"+name
            os.mkdir(newDir)
            newDir = pos + "\\campaigns\\"+name+"\\characters"
            os.mkdir(newDir)
            newDir = pos + "\\campaigns\\"+name+"\\NPCs"
            os.mkdir(newDir)
            newDir = pos + "\\campaigns\\"+name+"\\Settings"
            os.mkdir(newDir)
            newDir = pos + "\\campaigns\\"+name+"\\Encounters"
            os.mkdir(newDir)
            root.destroy()


    add_button = ttk.Button(frame, text='Add')
    add_button.grid(column=2, row=0, sticky='W')
    add_button.configure(command=add_button_clicked)

    # result label
    result_label = ttk.Label(frame)
    result_label.grid(row=1, columnspan=3)

    # add padding to the frame and show it
    frame.grid(padx=10, pady=10)


    # start the app
    root.mainloop()
