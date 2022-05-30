from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
import traceback
from tkinter import ttk
from trips import  TripLeg


class CreateTripLeg(Tk):

    def __init__(self, trip_legs):
        super().__init__()
        self.trip_legs = trip_legs 
        # print("My trip id is", self.id)
        self.title("Create Trip Leg")
        self.geometry("600x600")

        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 2)
        self.crete_traveller_label = Label(self, text="Create Trip Leg", bg="#20bebe")
        self.crete_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)

        # add components
        col =0
        row = 1

        self.strat_location_label = Label(self, text="Start Lcoation: ")
        self.strat_location_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.strat_location_entry = Entry(self)
        self.strat_location_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

        self.destination_label = Label(self, text="Destination: ")
        self.destination_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.destination_entry = Entry(self)
        self.destination_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           
        self.interest_points_label = Label(self, text="Points of interest: ")
        self.interest_points_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.interest_points_entry = Entry(self)
        self.interest_points_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.transport_label = Label(self, text="Transport Provider:")
        self.transport_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.transport_entry = Entry(self)
        self.transport_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.transport_mode_label = Label(self, text="Transport Mode: ")
        self.transport_mode_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)
        self.transport_mode_entry = ttk.Combobox(self, values=[ "plan", "ferry", "coach", "taxi"])
        self.transport_mode_entry.current(0)
        self.transport_mode_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)


        def save_trip_leg():
            try:
                start_location = self.strat_location_entry.get()
                destination = self.destination_entry.get()
                interest_points = self.interest_points_entry.get()
                transport_provider = self.transport_entry.get()
                transport_mode = self.transport_mode_entry.get()

                new_trip_leg = TripLeg(start_location, destination, interest_points, transport_provider, transport_mode)
                self.trip_legs.append(new_trip_leg)
                messagebox.showinfo(title="Success", message="Trip Leg created successfully")       
                self.destroy()
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showerror(title="Error", message="Failed to create traveller")
                self.system.refresh()
                
            # print(name,address,birth_date,emr_contact,ID_type,ID_num )

  
        self.submit_btn = Button(self, command= save_trip_leg ,text="Submit", bg = "#20bebe")
        self.submit_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)  

    
        

        # self.date_entry.insert("Date Format")    


