from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip, Traveller


class CreateTraveller(Tk):

    def __init__(self, system, trip_id):
        super().__init__()
        self.system = system
        self.id = trip_id 
        # print("My trip id is", self.id)
        self.title("Create Traveller")
        self.geometry("600x600")

        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 1)
        self.crete_traveller_label = Label(self, text="Create New Traveller", bg="#20bebe")
        self.crete_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)

        # add components
        col =0
        row = 1

        self.name_label = Label(self, text="Name:")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var= StringVar()
        self.name_entry = Entry(self, textvariable = self.name_var)
        self.name_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

        self.address_label = Label(self, text="Address:")
        self.address_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.address_var= StringVar()
        self.address_entry = Entry(self, textvariable = self.address_var)
        self.address_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           
        self.birth_date_label = Label(self, text="Birth Date:")
        self.birth_date_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.birth_date_var= StringVar()
        self.birth_date_entry = Entry(self, textvariable = self.birth_date_var)
        self.birth_date_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 

        self.emr_contact_label = Label(self, text="Emr Contact:")
        self.emr_contact_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.emr_contact_var= StringVar()
        self.emr_contact_entry = Entry(self,  textvariable = self.emr_contact_var)
        self.emr_contact_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.ID_label = Label(self, text="ID:")
        self.ID_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)

        self.ID_entry = ttk.Combobox(self, values=[ "passport", "driving_license", "national_id"])
        self.ID_entry.current(0)
        self.ID_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)

        self.ID_num_label = Label(self, text="ID Number:")
        self.ID_num_label.grid(column=col, row=row+5, sticky=E, padx=5, pady=10)
        self.ID_num_var= StringVar()
        self.ID_num_entry = Entry(self,  textvariable = self.ID_num_var)
        self.ID_num_entry.grid(column=col+1, row=row+5, sticky=W, pady=10)  

        def save_traveller():
            try:
                name = self.name_entry.get()
                address = self.address_entry.get()
                birth_date = self.birth_date_entry.get()
                emr_contact = self.emr_contact_entry.get()
                ID_type = self.ID_entry.get()
                ID_num = self.ID_num_entry.get()

                check_trip = self.system.search_trip(self.id)
                print('Check trip result is',check_trip)

                if check_trip == 0 or check_trip > 0 :
                    new_traveller = Traveller(name, address, birth_date, emr_contact)
                    new_traveller.add_id(ID_type, ID_num)
                    self.system.trips[check_trip].travellers.append(new_traveller)
                    messagebox.showinfo(title="Traveller Created", message="Traveller Created")

                    print(self.system.trips[0])
                self.destroy()
            except:
                messagebox.showerror(title="Error", message="Failed to create traveller")
                self.system.refresh()
                
            # print(name,address,birth_date,emr_contact,ID_type,ID_num )

  
        self.save_tra_btn = Button(self, command= save_traveller ,text="Submit", bg = "#20bebe")
        self.save_tra_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)  

    
        

        # self.date_entry.insert("Date Format")    


