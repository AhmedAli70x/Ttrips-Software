from tkinter import *

def Create(root):
    window=Toplevel(root)    
    window.geometry("900x500+50+50") # heightxwidth+x+y

    mainpanel = Canvas(window, width = 900, height = 500) # main screen
    mainpanel.pack()

    anyvar = StringVar() # the text in the entry
    entry = Entry(mainpanel, width = 40, font = ("Purisa", 12, "bold"), justify = "center", textvariable = anyvar) # the entry
    mainpanel.create_window(200, 100, window = entry)
    anyvar.set("This doesnt work!!!!!")

new = Create()
new.main_loop()