from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip, Traveller


class UpdateTraveller(Tk):

    def __init__(self, traveller):
        super().__init__()
        self.traveller  = traveller 


        self.title("View Travellers")
        self.geometry("700x800")
        self.configure(bg='white')
        self.wait_visibility()

        window = Frame(self, width=700, height=600, bg='white' )
        window.grid(column=0,row=0,padx=5, pady=10) 


        self.update_traveller_label = Label(window, text=f"Update Traveller: {self.traveller.name}", bg="#20bebe")
        self.update_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)


        def update_traveller():
            try:
                self.traveller.name = self.name_entry.get()
                self.traveller.address = self.address_entry.get()
                self.traveller.birth_date = self.birth_date_entry.get()
                self.traveller.emr_contact = self.ID_entry.get()

                self.traveller.gov_ids[0].id_type = self.name_entry.get()
                self.traveller.gov_ids[0].number = self.ID_num_entry.get()
                self.traveller.gov_ids[0].fullname = self.full_name_entry.get()
                self.traveller.gov_ids[0].expiry_date = self.expiray_date_entry.get()
                self.traveller.gov_ids[0].country = self.country_entry.get()
                self.destroy()
                messagebox.showinfo( title="Success", message=f"Traveller {self.traveller.name} Updated Successfully")
                print(f"Traveller {self.traveller.name} Updated Successfully")
                
            except:
                messagebox.showerror( title="Error", message=f"Failed to update {self.traveller.name}")

            
        col =0
        row = 1

        name = self.traveller.name
        address = self.traveller.address
        birthdate = self.traveller.birth_date
        emr_contact = self.traveller.emr_contact
        id_type = self.traveller.gov_ids[0].id_type
        pass_num = self.traveller.gov_ids[0].number
        full_name = self.traveller.gov_ids[0].full_name
        expiry_date = self.traveller.gov_ids[0].expiry_date
        country = self.traveller.gov_ids[0].country

        # self.combobox_num =0
        # if self.id_type == "passport":
        #     self.combobox_num =0
        # elif self.id_type == "driving_license":
        #     self.combobox_num =1
        # else:
        #     self.combobox_num =2
       


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
        self.ID_entry = ttk.Combobox(window, values=["passport"])
        self.ID_entry.current(0)
        self.ID_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)

        self.ID_num_label = Label(window, text="Passport Number:")
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


        self.country_label = Label(window, text="Country:")
        self.country_label.grid(column=col, row=row+8, sticky=E, padx=5, pady=10)
        self.country_var= StringVar(window, value=country)
        self.country_entry = Entry(window, textvariable= self.country_var )
        self.country_entry.grid(column=col+1, row=row+8, sticky=W, pady=10) 

        update_traveller_btn = Button(window, command= update_traveller ,text='Update', bg = '#20bebe')
        update_traveller_btn.grid(column=col+1, row=row+9, sticky=W, padx=5, pady=10)
     


