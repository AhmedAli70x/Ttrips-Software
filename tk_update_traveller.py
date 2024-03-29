from cgitb import text
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip, Traveller
from validation import Validation as v
import traceback


class UpdateTraveller(Tk):

    def __init__(self, traveller):
        super().__init__()
        self.traveller  = traveller 


        self.title("Update Travelles")
        self.geometry("500x600")
  
        self.wait_visibility()

        window = Frame(self, width=700, height=600, )
        window.grid(column=0,row=0,padx=5, pady=10) 


        self.update_traveller_label = Label(window, text=f"Update Traveller: {self.traveller.name}", bg="#20bebe")
        self.update_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)


        def update_traveller():
            try:

                name = self.name_entry.get()
                address = self.address_entry.get()
                birth_date = self.birth_date_entry.get()
                emr_contact = self.emr_contact_entry.get()
                ID_type = self.ID_entry.get()
                ID_num = self.ID_num_entry.get()
                full_name = self.full_name_entry.get()
                expiry_date = self.expiray_date_entry.get()
                country = self.country_entry.get()
                #validate trip lege entries befor updating
                checK_traveller = v.check_traveller(name, address, birth_date, emr_contact, ID_num, full_name, expiry_date, country)
                if checK_traveller:
                    self.traveller.name = name
                    self.traveller.address = address
                    self.traveller.birth_date = birth_date
                    self.traveller.emr_contact = emr_contact
                    if self.traveller.gov_ids:
                        self.traveller.gov_ids[0].id_type = ID_type
                        self.traveller.gov_ids[0].number =ID_num
                        self.traveller.gov_ids[0].fullname = full_name
                        self.traveller.gov_ids[0].expiry_date = expiry_date
                        self.traveller.gov_ids[0].country = country
                    else:
                        self.traveller.create_id(ID_type, ID_num, full_name,  expiry_date, country)
                    self.destroy()
                    messagebox.showinfo( title="Success", message=f"Traveller {self.traveller.name} Updated Successfully")
                    # print(f"Traveller {self.traveller.name} Updated Successfully")
                
            except Exception:
                traceback.print_exc()
                messagebox.showerror( title="Error", message=f"Failed to update {self.traveller.name}")

            
        col =0
        row = 1

        name = self.traveller.name
        address = self.traveller.address
        birthdate = self.traveller.birth_date
        emr_contact = self.traveller.emr_contact
        if self.traveller.gov_ids:
            id_type = self.traveller.gov_ids[0].id_type
            pass_num = self.traveller.gov_ids[0].number
            full_name = self.traveller.gov_ids[0].full_name
            expiry_date = self.traveller.gov_ids[0].expiry_date
            country = self.traveller.gov_ids[0].country
        else:
            id_type = 'passport'
            pass_num = 'NA'
            full_name = 'NA'
            expiry_date = 'NA'
            country = 'NA'





        self.name_label = Label(window, text="Name: ")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var1= StringVar(self, value= name)
        self.name_entry = Entry(window, textvariable=self.name_var1)
        self.name_entry.grid(column=col+1, row=row, sticky=E, padx=5, pady=10)

        self.address_label = Label(window, text="Address: ")
        self.address_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.address_var= StringVar(self, value= address)
        self.address_entry = Entry(window, textvariable = self.address_var)
        self.address_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           
        self.birth_date_label = Label(window, text="Birth Date: ")
        self.birth_date_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.birth_date_var= StringVar(self, value= birthdate)
        self.birth_date_entry = Entry(window, textvariable = self.birth_date_var)
        self.birth_date_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 

        self.emr_contact_label = Label(window, text="Emr Contact:")
        self.emr_contact_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.emr_contact_var= StringVar(self, value= emr_contact)
        self.emr_contact_entry = Entry(window,  textvariable = self.emr_contact_var)
        self.emr_contact_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.ID_label = Label(window, text="ID:")
        self.ID_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)
        self.ID_entry = ttk.Combobox(window, text= id_type,values=["passport", "driving_license", "national_id"])
        self.ID_entry.current(0)
        self.ID_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)

        self.ID_num_label = Label(window, text="ID Number: ")
        self.ID_num_label.grid(column=col, row=row+5, sticky=E, padx=5, pady=10)
        self.ID_num_var= StringVar(window, value=pass_num)
        self.ID_num_entry = Entry(window, textvariable = self.ID_num_var)
        self.ID_num_entry.grid(column=col+1, row=row+5, sticky=W, pady=10) 

        
        self.full_name_label = Label(window, text="Full Name:")
        self.full_name_label.grid(column=col, row=row+6, sticky=E, padx=5, pady=10)
        self.full_name_var= StringVar(window, value=full_name)
        self.full_name_entry = Entry(window, textvariable= self.full_name_var)
        self.full_name_entry.grid(column=col+1, row=row+6, sticky=W, pady=10)  

        self.expiray_date_label = Label(window, text="Expiry Date:")
        self.expiray_date_label.grid(column=col, row=row+7, sticky=E, padx=5, pady=10)
        self.expiry_date_var= StringVar(window, value=expiry_date)
        self.expiray_date_entry = Entry(window, textvariable= self.expiry_date_var)
        self.expiray_date_entry.grid(column=col+1, row=row+7, sticky=W, pady=10)  


        self.country_label = Label(window, text="Country: ")
        self.country_label.grid(column=col, row=row+8, sticky=E, padx=5, pady=10)
        self.country_var= StringVar(window, value=country)
        self.country_entry = Entry(window, textvariable= self.country_var )
        self.country_entry.grid(column=col+1, row=row+8, sticky=W, pady=10) 

        update_traveller_btn = Button(window, command= update_traveller ,text='Update', bg = '#20bebe')
        update_traveller_btn.grid(column=col+1, row=row+9, sticky=W, padx=5, pady=10)
     


