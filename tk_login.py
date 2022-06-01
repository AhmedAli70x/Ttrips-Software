from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
import traceback
from trips import Trip, Traveller
from tk_coodinator_gui import CoodinatorMenu
from tk_main import MainMenu
from tk_manager_gui import ManagerMenu
class LoginGUI(Tk):

    def __init__(self, system= None):
        super().__init__()
        self.system = system
        self.title("Login")
        self.geometry("300x300")
        self.resizable(10, 10)

        self.columnconfigure(0, weight= 2)
        self.columnconfigure(1, weight= 2)
        self.crete_traveller_label = Label(self, text="Solent Trip System", bg="#20bebe", font=("Arial", 12))
        
        self.crete_traveller_label.grid( column= 1 , row=0, sticky=W, padx=20, pady=20)

        col =0
        row = 1

        self.username_label = Label(self, text="Username:")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_var= StringVar()
        self.username_entry = Entry(self, textvariable = self.username_var)
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 


        def login():
            username = self.username_entry.get()
            system.login(username)
            #Chech login role and direct him/her to the prper page
            if self.system.login_user == "coodinator":
                self.destroy()
                main_gui = CoodinatorMenu(self.system)
                main_gui.mainloop()
            elif self.system.login_user == "manager":
                self.destroy()
                main_gui = ManagerMenu(self.system)
                main_gui.mainloop()
            elif self.system.login_user == "admin":
                self.destroy()
                main_gui = MainMenu(self.system)
                main_gui.mainloop()


  
        self.save_tra_btn = Button(self, command= login ,text="Login", bg = "#20bebe")
        self.save_tra_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)  

 


