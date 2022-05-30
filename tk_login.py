from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
import traceback
from trips import Trip, Traveller

from tk_main import MainMenu
class LoginGUI(Tk):

    def __init__(self, system= None):
        super().__init__()
        self.system = system
        self.title("Login")
        self.geometry("300x300")

        self.columnconfigure(0, weight= 2)
        self.columnconfigure(1, weight= 2)
        self.crete_traveller_label = Label(self, text="Solent Trip System", bg="#20bebe", font=("Arial", 12))
        
        self.crete_traveller_label.grid( column= 1 , row=0, sticky=W, padx=20, pady=20)

        # add components
        col =0
        row = 1

        self.username_label = Label(self, text="Username:")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_var= StringVar()
        self.username_entry = Entry(self, textvariable = self.username_var)
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

        self.password_label = Label(self, text="Password:")
        self.password_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.password_var= StringVar()
        self.password_entry = Entry(self, textvariable = self.password_var)
        self.password_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           

        def login():
            username = self.username_entry.get()
            password = self.password_entry.get()
            system.login(username, password)
            if self.system.login_user == "admin":
                self.destroy()
                main_gui = MainMenu(self.system)
                main_gui.mainloop()
            # try:
            #     username = self.username_entry.get()
            #     password = self.password_entry.get()
            #     system.login(username, password)
            #     if system.login_user == "admin":
            #         main_gui = MainMenu(self.system)
            #         main_gui.mainloop()
 
            # except ZeroDivisionError:
            #     traceback.print_exc()
            #     messagebox.showerror(title="Error", message="Failed to Login")
    
                
            # print(name,address,birth_date,emr_contact,ID_type,ID_num )

  
        self.save_tra_btn = Button(self, command= login ,text="Login", bg = "#20bebe")
        self.save_tra_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)  



        # self.date_entry.insert("Date Format")    


