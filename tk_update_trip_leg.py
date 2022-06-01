from inspect import trace
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
import traceback
from trips import Trip, Traveller
from validation import Validation as v


class UpdateTripLeg(Tk):

    def __init__(self, trip_leg):
        super().__init__()
        self.trip_leg  = trip_leg 
        self.title("Update Trip Leg")
        self.geometry("500x600")
        self.configure(bg='white')
        self.wait_visibility()

        window = Frame(self, width=700, height=600, bg='white' )
        window.grid(column=0,row=0,padx=5, pady=10) 


        self.update_traveller_label = Label(window, text=f"Update Trip Leg ", bg="#20bebe")
        self.update_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)


        def update_trip_leg():
            try:
                start_location = self.strat_location_entry.get()
                destination = self.destination_entry.get()
                interest_point = self.interest_points_entry.get()
                transport_provider = self.transport_entry.get()
                transport_mode = self.transport_mode_entry.get()

                check_trip_leg = v.check_trip_leg(start_location, destination, interest_point, transport_provider)
                if check_trip_leg:
                    self.trip_leg.starting_location = start_location
                    self.trip_leg.destination = destination
                    self.trip_leg.point_of_interest = interest_point
                    self.trip_leg.transport_provider = transport_provider
                    self.trip_leg.transport_mode = transport_mode
                    self.destroy()
                    messagebox.showinfo( title="Success", message=f"Trip Leg Updated Successfully")
                
            except Exception:
                traceback.print_exc()
                messagebox.showerror( title="Error", message=f"Failed to update Trip Leg ")

            
        col =0
        row = 1

        starting_location = self.trip_leg.starting_location
        destination = self.trip_leg.destination
        point_of_interest = self.trip_leg.point_of_interest
        transport_provider = self.trip_leg.transport_provider
        transport_mode = self.trip_leg.transport_mode
   
        

        self.strat_location_label = Label(self, text="Start Lcoation: ")
        self.strat_location_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.start_location_var = StringVar(self, value= starting_location)
        self.strat_location_entry = Entry(self, textvariable=self.start_location_var )
        self.strat_location_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

        self.destination_label = Label(self, text="Destination: ")
        self.destination_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.destination_var = StringVar(self, value= destination)
        self.destination_entry = Entry(self, textvariable=self.destination_var)
        self.destination_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)     
           
        self.interest_points_label = Label(self, text="Points of interest: ")
        self.interest_points_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.point_of_interest_var = StringVar(self, value= point_of_interest)
        self.interest_points_entry = Entry(self, textvariable=self.point_of_interest_var)
        self.interest_points_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.transport_label = Label(self, text="Transport Provider:")
        self.transport_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.transport_provider_var = StringVar(self, value= transport_provider)
        self.transport_entry = Entry(self, textvariable = self.transport_provider_var)
        self.transport_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.transport_mode_label = Label(self, text="Transport Mode: ")
        self.transport_mode_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)
        self.transport_mode_var = StringVar(self, value=transport_mode)
        self.transport_mode_entry = ttk.Combobox(self, textvariable= self.transport_mode_var, values=[ "plan", "ferry", "coach", "taxi"])
        self.transport_mode_entry.grid(column=col+1, row=row+4, sticky=W, pady=10)
            
        update_btn = Button(self, command = update_trip_leg ,text='Update', bg = '#20bebe')
        update_btn.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)


  
        

        # self.date_entry.insert("Date Format")    


