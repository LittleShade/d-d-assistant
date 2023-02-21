import tkinter as tk
from tkinter import ttk
import os

def viewmenu(pos):

    #get current dir and campaigns


    # root window
    root = tk.Tk()
    root.title('Campaign viewer')
    root.geometry('300x200')
  



    # frame
    frame = ttk.Frame(root)


    # field options
    options = {'padx': 5, 'pady': 5}

    # character label
    temperature_label = ttk.Label(frame, text='pick a character')
    temperature_label.grid(column=0, row=0, sticky='W', **options)

    # character entry
    existing_character=os.listdir(pos+"\\characters")
    
    try:
        character = tk.StringVar(existing_character[0])
    except:
        campaign = tk.StringVar(root)
    campaign_entry = tk.OptionMenu(frame, campaign, existing_character)
    campaign_entry.grid(column=1, row=0, **options)
    campaign_entry.focus()



    # open button

    def open_button_clicked():
        """  Handle open button click event 
        """
        pos=os.getcwd()
        existing_campaigns=os.listdir(pos+ "\\campaigns\\"+campaign_entry.get())
        
        root.destroy()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=0, sticky='W')
    convert_button.configure(command=open_button_clicked)

    # NPC label
    NPC_label = ttk.Label(frame, text='pick a NPC')
    NPC_label.grid(column=0, row=1, sticky='W', **options)

    # NPC entry
    existing_NPCs=os.listdir(pos+"\\NPCs")
    
    try:
        NPC = tk.StringVar(existing_NPCs[0])
    except:
        NPC = tk.StringVar(root)
    NPC_entry = tk.OptionMenu(frame, campaign, existing_NPCs)
    NPC_entry.grid(column=1, row=1, **options)
    NPC_entry.focus()



    # open button

    def NPCopen_button_clicked():
        """  Handle open button click event 
        """
        existing_campaigns=os.listdir(pos+ "\\campaigns\\"+NPC_entry.get())
        
        root.destroy()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=1, sticky='W')
    convert_button.configure(command=NPCopen_button_clicked)

    # Setting label
    Setting_label = ttk.Label(frame, text='pick a Setting')
    Setting_label.grid(column=0, row=2, sticky='W', **options)

    # Setting entry
    existing_Setting=os.listdir(pos+"\\Settings")
    
    try:
        Setting = tk.StringVar(existing_Setting[0])
    except:
        Setting = tk.StringVar(root)
    Setting_entry = tk.OptionMenu(frame, Setting, existing_Setting)
    Setting_entry.grid(column=1, row=2, **options)
    Setting_entry.focus()



    # open button

    def Settingsopen_button_clicked():
        """  Handle open button click event 
        """
        pos=os.getcwd()
        existing_Settings=os.listdir(pos+ "\\campaigns\\"+Setting_entry.get())
        
        root.destroy()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=2, sticky='W')
    convert_button.configure(command=Settingsopen_button_clicked)

    # Encounters label
    Encounters_label = ttk.Label(frame, text='pick an Encounter')
    Encounters_label.grid(column=0, row=3, sticky='W', **options)

    # Encounters entry
    existing_Encounters=os.listdir(pos+"\\Encounters")
    
    try:
        Encounters = tk.StringVar(existing_Encounters[0])
    except:
        Encounters = tk.StringVar(root)
    Encounters_entry = tk.OptionMenu(frame, Encounters, existing_Encounters)
    Encounters_entry.grid(column=1, row=3, **options)
    Encounters_entry.focus()



    # open button

    def Encountersopen_button_clicked():
        """  Handle open button click event 
        """
        pos=os.getcwd()
        existing_Settings=os.listdir(pos+ "\\campaigns\\"+Encounters_entry.get())
        
        root.destroy()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=3, sticky='W')
    convert_button.configure(command=Encountersopen_button_clicked)

    # add padding to the frame and show it
    frame.grid(padx=10, pady=10)


    # start the app
    root.mainloop()
