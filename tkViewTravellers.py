from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from tkUpdateTraveller import UpdateTraveller
from trips import Trip, Traveller


class ViewTravellers(Tk):

    def __init__(self, system, trip_id):
        super().__init__()
        self.system = system
        self.id = trip_id 
        self.title("View Travellers")
        self.geometry("700x600")
        self.configure(bg='white')
      
        self.view_traveller_label = Label(self, text="View Travellers", bg="#20bebe")
        self.view_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)



        def update_traveller(traveller_id):
            print(f"Update traveller {id}") 
            update_traveller = UpdateTraveller(self.system, self.id, traveller_id)
            update_traveller.mainloop()
        # add components
        col =0
        row = 1

        self.tra_name_label = Label(self, text="Name")
        self.tra_name_label.grid(column=col, row=row, sticky=W, padx=5, pady=10)
        self.tra_address_label = Label(self, text="Address")
        self.tra_address_label.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)
        self.tra_birth_date_label = Label(self, text="Birth Date")
        self.tra_birth_date_label.grid(column=col+2, row=row, sticky=W, padx=5, pady=10)
        self.tra_emr_contact_label = Label(self, text="Emr Contact")
        self.tra_emr_contact_label.grid(column=col+3, row=row, sticky=W, padx=5, pady=10)
        self.tra_ID_label = Label(self, text="ID")
        self.tra_ID_label.grid(column=col+4, row=row, sticky=W, padx=5, pady=10)
        self.tra_ID_num_label = Label(self, text="ID Number")
        self.tra_ID_num_label.grid(column=col+5, row=row, sticky=W, padx=5, pady=10)

        buttons = []
        buttons2 = []
        buttons3 = []
        #Check if the trip has travellers, 4th element is the travellers list
        if self.system.trips[self.id].travellers:
            travellers_number = len(self.system.trips[self.id].travellers)
            travellers = self.system.trips[self.id].travellers
            for i in range(travellers_number):

                traveller_name = travellers[i].name
                traveller_view_label = Label(self, text=traveller_name)
                traveller_view_label.grid(column=0, row=row+1+i, sticky=W, padx=10, pady=10)

                traveller_address =  travellers[i].address
                address_view_label = Label(self, text=traveller_address)
                address_view_label.grid(column=1, row=row+1+i, sticky=W, padx=10, pady=10)


                traveller_birth_date = travellers[i].birth_date
                traveller_birth_label = Label(self, text=traveller_birth_date)
                traveller_birth_label.grid(column=2, row=row+1+i, sticky=W, padx=10, pady=10)

                emr_contact = travellers[i].emr_contact
                emr_contact_label = Label(self, text=emr_contact)
                emr_contact_label.grid(column=3, row=row+1+i, sticky=W, padx=10, pady=10)

                if travellers[i].gov_ids:
                    ID_type = travellers[i].gov_ids[0].id_type
                    ID_type_label = Label(self, text=ID_type)
                    ID_type_label.grid(column=4, row=row+1+i, sticky=W, padx=10, pady=10)

                    ID_number = travellers[i].gov_ids[0].number
                    ID_number_label = Label(self, text=ID_number)
                    ID_number_label.grid(column=5, row=row+1+i, sticky=W, padx=10, pady=10)
                else:
                    ID_type = None
                    ID_type_label = Label(self, text=ID_type)
                    ID_type_label.grid(column=4, row=row+1+i, sticky=W, padx=10, pady=10)

                    ID_number = None
                    ID_number_label = Label(self, text=ID_number)
                    ID_number_label.grid(column=5, row=row+1+i, sticky=W, padx=10, pady=10)
                    
                    
                buttons.append(Button(self, command=lambda: update_traveller(i) ,text='Update Traveller', bg = '#20bebe'))
                buttons[i].grid(column=6, row=row+1+i, sticky=W, padx=5, pady=10)

                # buttons2.append(Button(self, command=lambda: create_trip_leg(i) ,text='Add Trip Leg', bg = '#20bebe'))
                # buttons2[i].grid(column=col+4, row=row+6+i, sticky=W, padx=5, pady=10)

                # buttons3.append(Button(self.view_trips, command=lambda: view_travellers(i) ,text='View Travellers', bg = '#20bebe'))
                # buttons3[i].grid(column=col+5, row=row+6+i, sticky=W, padx=5, pady=10)
            

        else:
            messagebox.showinfo(title="No Travellers", message="No Travellers to display",)



  
        

        # self.date_entry.insert("Date Format")    


