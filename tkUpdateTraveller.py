from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip, Traveller


class UpdateTraveller(Tk):

    def __init__(self, system, trip_id, traveller_id):
        super().__init__()
        self.system = system
        self.id = trip_id 
        self.traveller_id = traveller_id

        self.title("View Travellers")
        self.geometry("700x600")
        self.configure(bg='white')
        self.wait_visibility()

        window = Frame(self, width=700, height=600, bg='white' )
        window.grid(column=0,row=0,padx=5, pady=10) 

  
        # self.update_traveller = Frame(window, width=700, height=600, bg='white' )
        # self.update_traveller.grid(column=0,row=0,padx=5, pady=10)

        self.update_traveller_label = Label(window, text=f"Update Travellers {self.traveller_id}", bg="#20bebe")
        self.update_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)


        def Create(self):
            window=Toplevel(self)    
            window.geometry("900x500+50+50") # heightxwidth+x+y

            mainpanel = Canvas(window, width = 900, height = 500) # main screen
            mainpanel.pack()

            anyvar = StringVar() # the text in the entry
            entry = Entry(mainpanel, width = 40, font = ("Purisa", 12, "bold"), justify = "center", textvariable = anyvar) # the entry
            mainpanel.create_window(200, 100, window = entry)
            anyvar.set("This doesnt work!!!!!")


        def update_traveller():
            self.name_var1.set(name)
            print(f"update traveller {traveller_id}")
            pass
        # add components
        col =0
        row = 1

        name = self.system.trips[trip_id].travellers[traveller_id].name
        address = self.system.trips[trip_id].travellers[traveller_id].address
        birthdate = self.system.trips[trip_id].travellers[traveller_id].birth_date
        emr_contact = self.system.trips[trip_id].travellers[traveller_id].emr_contact
        print(name, address)

        self.name_label = Label(window, text="Name: ")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var1= StringVar()
        self.name_entry = Entry(window, textvariable=self.name_var1)
        self.name_var1.set(name)
        self.name_entry.grid(column=col+1, row=row, sticky=E, padx=5, pady=10)
        

        self.address_label = Label(window, text="Address: ")
        self.address_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.address_var= StringVar()
        self.address_entry = Entry(window, textvariable = self.address_var)
        self.address_var.set(address)
        self.address_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           
        self.birth_date_label = Label(window, text="Birth Date: ")
        self.birth_date_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.birth_date_var= StringVar()
        self.birth_date_entry = Entry(window, textvariable = self.birth_date_var)
        self.birth_date_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 

        self.emr_contact_label = Label(window, text="Emr Contact:")
        self.emr_contact_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.emr_contact_var= StringVar()
        self.emr_contact_entry = Entry(window,  textvariable = self.emr_contact_var)
        self.emr_contact_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.ID_label = Label(window, text="ID:")
        self.ID_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)

        self.ID_entry = ttk.Combobox(window, values=[ "passport", "driving_license", "national_id"])
        self.ID_entry.current(0)
        self.ID_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)

        self.ID_num_label = Label(window, text="ID Number:")
        self.ID_num_label.grid(column=col, row=row+5, sticky=E, padx=5, pady=10)
        self.ID_num_var= StringVar()
        self.ID_num_entry = Entry(window,  textvariable = self.ID_num_var)
        self.ID_num_entry.grid(column=col+1, row=row+5, sticky=W, pady=10) 
            
        update_btn = Button(window, command=lambda: update_traveller() ,text='Update', bg = '#20bebe')
        update_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)


  
        

        # self.date_entry.insert("Date Format")    


