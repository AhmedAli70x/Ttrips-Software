from cgitb import text
from inspect import trace
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
import traceback
from trips import Trip, Traveller


class UpdateUser(Tk):

    def __init__(self, user):
        super().__init__()
        self.user  = user 
        self.title("Update User")
        self.geometry("500x500")
        self.configure(bg='white')
        self.wait_visibility()

  


        self.update_traveller_label = Label(self, text=f"Update User ", bg="#20bebe")
        self.update_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)


        def update_user():
            try:
                self.trip_leg.starting_location = self.strat_location_entry.get()
                self.trip_leg.destination = self.destination_entry.get()
                self.trip_leg.point_of_interest = self.interest_points_entry.get()
                self.trip_leg.transport_provider = self.transport_entry.get()
                print("Trans mode is", self.transport_mode_entry.get())
                self.trip_leg.transport_mode = self.transport_mode_entry.get()
                self.destroy()
                messagebox.showinfo( title="Success", message=f"Trip Leg Updated Successfully")
                # print(f"Traveller  Updated Successfully")
                
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showerror( title="Error", message=f"Failed to update Trip Leg ")

    

        form_username = self.user.username
        form_name = self.user.name
        form_phone = self.user.phone
        form_role = self.user.role
   
        
  
        def update_user():
            try:
                    
                username = username_entry.get()
                user_name =user_name_entry.get()
                phone = phone_entry.get()
                role = role_entry.get()


                self.user.username = username
                self.user.name = user_name
                self.user.phone = phone
                
                self.user.role = role
                print(self.user.role)

                self.destroy()
                messagebox.showinfo( title="Success", message=f"User Updated Successfully")
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showerror(title="Error", message=f"User Update Error")

        
        col =0
        row = 1
        username_label = Label(self, text="Username: ")
        username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_var= StringVar(self, value=form_username)
        username_entry = Entry(self, textvariable= self.username_var)
        username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        user_name_label = Label(self, text="Name: ")
        user_name_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.name_var= StringVar(self, value=form_name)
        user_name_entry = Entry(self,  textvariable= self.name_var)
        user_name_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        phone_label = Label(self, text="Phone: ")
        phone_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.phone_var= StringVar(self, value=form_phone)
        phone_entry = Entry(self, textvariable= self.phone_var)
        phone_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        role_label = Label(self, text="Role: ")
        role_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.role_var = StringVar(self, value=form_role)
        role_entry = ttk.Combobox(self, textvariable=self.role_var,  values=['c', 'm'])
        role_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  
            
        create_user_btn = Button(self, command= update_user ,text= "Save", bg = "#20bebe")
        create_user_btn.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10)


