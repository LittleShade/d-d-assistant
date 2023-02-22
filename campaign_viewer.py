import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import os

# field options
options = {'padx': 5, 'pady': 5}


def viewmenu(pos):

    # open button action

    def open_button_clicked(docType,docName):
        """  Handle open button click event 
        """
        file=open(pos+ "\\"+docType+"\\"+docName,"r")
        info=file.readlines()
        reader=tk.Toplevel()
        reader.title=docName
        text=scrolledtext.ScrolledText(master=reader)
        text.insert(tk.END, info)
        text.pack()

    #get current dir and campaignss


    # root window
    root = tk.Tk()
    root.title('Campaign viewer')
    root.geometry('500x200')
  



    # frame
    frame = ttk.Frame(root)




###########################################################################

    # character label
    character_label = ttk.Label(frame, text='pick a character')
    character_label.grid(column=0, row=0, sticky='W', **options)

    # character entry
    existing_character=os.listdir(pos+"\\characters")
    
    try:
        character = tk.StringVar(existing_character[0])
    except:
        character = tk.StringVar(root)
    character_entry = tk.OptionMenu(frame, character, *existing_character)
    character_entry.grid(column=1, row=0, **options)
    character_entry.focus()
        

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=0, sticky='W')
    convert_button.configure(command=lambda: open_button_clicked("characters",character.get()))

    #new character button action

    def new_character_button_clicked():
        """handle new character button clicked
        """
        #make top level
        newchr= tk.Toplevel()
        newchr.title("new character")

        #make label for entry
        title_label= ttk.Label(master=newchr,text="Enter character name:")
        title_label.pack()

        #make title entry form
        title_entry=ttk.Entry(master=newchr, width=10)
        title_entry.pack()

        #make label for entry
        info_label= ttk.Label(master=newchr,text="Enter character info:")
        info_label.pack()

        #make chr info entry form
        info_entry=scrolledtext.ScrolledText(master=newchr, width=50,height=30)
        info_entry.pack()

        # add button pressed
        def add_button_pressed():
            name=title_entry.get()
            info=info_entry.get("1.0",'end-1c')
            newChrFile=open(pos+"\\characters\\"+name+".txt","w")
            newChrFile.write(info)
            newChrFile.close()
            newchr.destroy()

        add_button=ttk.Button(master=newchr,text="save")
        add_button.configure(command=add_button_pressed)
        add_button.pack()

        newchr.mainloop()


    newchr_button = ttk.Button(frame, text='new')
    newchr_button.grid(column=3, row=0, sticky='W')
    newchr_button.configure(command=new_character_button_clicked) 

###########################################################################

    # NPC label
    NPC_label = ttk.Label(frame, text='pick a NPC')
    NPC_label.grid(column=0, row=1, sticky='W', **options)

    # NPC entry
    existing_NPCs=os.listdir(pos+"\\NPCs")
    
    try:
        NPC = tk.StringVar(existing_NPCs[0])
    except:
        NPC = tk.StringVar(root)
    NPC_entry = tk.OptionMenu(frame, NPC, *existing_NPCs)
    NPC_entry.grid(column=1, row=1, **options)
    NPC_entry.focus()



    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=1, sticky='W')
    convert_button.configure(command=lambda: open_button_clicked("NPCs",NPC.get()))

    #new NPC button action

    def new_NPC_button_clicked():
        """handle new NPC button clicked
        """
        #make top level
        newNPC= tk.Toplevel()
        newNPC.title("new NPC")

        #make label for entry
        title_label= ttk.Label(master=newNPC,text="Enter NPC name:")
        title_label.pack()

        #make title entry form
        title_entry=ttk.Entry(master=newNPC, width=10)
        title_entry.pack()

        #make label for entry
        info_label= ttk.Label(master=newNPC,text="Enter NPC info:")
        info_label.pack()

        #make NPC info entry form
        info_entry=scrolledtext.ScrolledText(master=newNPC, width=50,height=30)
        info_entry.pack()

        # add button pressed
        def add_button_pressed():
            name=title_entry.get()
            info=info_entry.get("1.0",'end-1c')
            newNPCFile=open(pos+"\\NPCs\\"+name+".txt","w")
            newNPCFile.write(info)
            newNPCFile.close()
            newNPC.destroy()

        add_button=ttk.Button(master=newNPC,text="save")
        add_button.configure(command=add_button_pressed)
        add_button.pack()

        newNPC.mainloop()


    newchr_button = ttk.Button(frame, text='new')
    newchr_button.configure(command=new_NPC_button_clicked)
    newchr_button.grid(column=3, row=1, sticky='W')

###########################################################################

    # Setting label
    Setting_label = ttk.Label(frame, text='pick a Setting')
    Setting_label.grid(column=0, row=2, sticky='W', **options)

    # Setting entry
    existing_Setting=os.listdir(pos+"\\Settings")
    
    try:
        Setting = tk.StringVar(existing_Setting[0])
    except:
        Setting = tk.StringVar(root)
    Setting_entry = tk.OptionMenu(frame, Setting, *existing_Setting)
    Setting_entry.grid(column=1, row=2, **options)
    Setting_entry.focus()


    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=2, sticky='W')
    convert_button.configure(command=lambda: open_button_clicked("Settings",Setting.get()))

    #new setting button action

    def new_Setting_button_clicked():
        """handle new NPC button clicked
        """
        #make top level
        newSetting= tk.Toplevel()
        newSetting.title("new NPC")

        #make label for entry
        title_label= ttk.Label(master=newSetting,text="Enter setting name:")
        title_label.pack()

        #make title entry form
        title_entry=ttk.Entry(master=newSetting, width=10)
        title_entry.pack()

        #make label for entry
        info_label= ttk.Label(master=newSetting,text="Enter setting info:")
        info_label.pack()

        #make setting info entry form
        info_entry=scrolledtext.ScrolledText(master=newSetting, width=50,height=30)
        info_entry.pack()

        # add button pressed
        def add_button_pressed():
            name=title_entry.get()
            info=info_entry.get("1.0",'end-1c')
            newSettingFile=open(pos+"\\Settings\\"+name+".txt","w")
            newSettingFile.write(info)
            newSettingFile.close()
            newSetting.destroy()

        add_button=ttk.Button(master=newSetting,text="save")
        add_button.configure(command=add_button_pressed)
        add_button.pack()

        newSetting.mainloop()


    newchr_button = ttk.Button(frame, text='new')
    newchr_button.configure(command=new_Setting_button_clicked)
    newchr_button.grid(column=3, row=2, sticky='W')

###########################################################################

    # Encounters label
    Encounters_label = ttk.Label(frame, text='pick an Encounter')
    Encounters_label.grid(column=0, row=3, sticky='W', **options)

    # Encounters entry
    existing_Encounters=os.listdir(pos+"\\Encounters")
    
    try:
        Encounters = tk.StringVar(existing_Encounters[0])
    except:
        Encounters = tk.StringVar(root)
    Encounters_entry = tk.OptionMenu(frame, Encounters, *existing_Encounters)
    Encounters_entry.grid(column=1, row=3, **options)
    Encounters_entry.focus()

    #set up open button    

    convert_button = ttk.Button(frame, text='open')
    convert_button.grid(column=2, row=3, sticky='W')
    convert_button.configure(command=lambda: open_button_clicked("Encounters",Encounters.get()))

    #new encounter button pressed

    def new_Encounter_button_clicked():
        """handle new encounter button clicked
        """
        #make top level
        newEncounter= tk.Toplevel()
        newEncounter.title("new encounter")

        #make label for entry
        title_label= ttk.Label(master=newEncounter,text="Enter encounter name:")
        title_label.pack()

        #make title entry form
        title_entry=ttk.Entry(master=newEncounter, width=10)
        title_entry.pack()

        #make label for entry
        info_label= ttk.Label(master=newEncounter,text="Enter encounter info:")
        info_label.pack()

        #make NPC info entry form
        info_entry=scrolledtext.ScrolledText(master=newEncounter, width=50,height=30)
        info_entry.pack()

        # add button pressed
        def add_button_pressed():
            name=title_entry.get()
            info=info_entry.get("1.0",'end-1c')
            newEncounterfile=open(pos+"\\Encounters\\"+name+".txt","w")
            newEncounterfile.write(info)
            newEncounterfile.close()
            newEncounter.destroy()

        add_button=ttk.Button(master=newEncounter,text="save")
        add_button.configure(command=add_button_pressed)
        add_button.pack()

        newEncounter.mainloop()


    newchr_button = ttk.Button(frame, text='new')
    newchr_button.configure(command=new_Encounter_button_clicked)
    newchr_button.grid(column=3, row=3, sticky='W')

###########################################################################

    # add padding to the frame and show it
    frame.grid(padx=10, pady=10)


    # start the app
    root.mainloop()
