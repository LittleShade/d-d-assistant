import tkinter as tk
from tkinter import ttk
import os

def searchmenu():

    #get current dir and campaigns

    pos=os.getcwd()
    existing_campaigns=os.listdir(pos+ "\\campaigns")

    # root window
    root = tk.Tk()
    root.title('Campaign search')
    root.geometry('300x70')
    root.resizable(False, False)



    # frame
    frame = ttk.Frame(root)


    # field options
    options = {'padx': 5, 'pady': 5}

    # campaign label
    temperature_label = ttk.Label(frame, text='pick a campaign')
    temperature_label.grid(column=0, row=0, sticky='W', **options)

    # campaign entry
    try:
        campaign = tk.StringVar(existing_campaigns[0])
    except:
        campaign = tk.StringVar(root)
    campaign_entry = tk.OptionMenu(frame, campaign, existing_campaigns)
    campaign_entry.grid(column=1, row=0, **options)
    campaign_entry.focus()



    # open button

    def open_button_clicked():
        """  Handle open button click event 
        """
        root.destroy()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=0, sticky='W')
    convert_button.configure(command=open_button_clicked)

    # result label
    result_label = ttk.Label(frame)
    result_label.grid(row=1, columnspan=3)

    # add padding to the frame and show it
    frame.grid(padx=10, pady=10)


    # start the app
    root.mainloop()
