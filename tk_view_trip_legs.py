from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip, Traveller
from tk_update_trip_leg import UpdateTripLeg

class ViewTripLegs(Tk):

    def __init__(self, trip_legs):
        super().__init__()
        self.trip_legs = trip_legs
   
        self.title("View Trip Legs")
        self.geometry("900x600")
        self.configure(bg='white')
      
        self.view_traveller_label = Label(self, text="View Trip Legs", bg="#20bebe")
        self.view_traveller_label.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)



        def update_trip_leg(trip_leg):
            self.destroy()
            # print(f"Update  {trip_leg}") 
            update_traveller = UpdateTripLeg(trip_leg)
            update_traveller.mainloop()


        def delete_trip_leg(trip_leg_id):
            print(f"Delete {trip_leg_id}") 
            self.trip_legs.pop(trip_leg_id)
            self.destroy()
            self.__init__(self.trip_legs)

        col =0
        row = 1

        self.strat_location_label = Label(self, text="Strating Location")
        self.strat_location_label.grid(column=col, row=row, sticky=W, padx=5, pady=10)
        self.destination_label = Label(self, text="Destination")
        self.destination_label.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)
        self.interest_points_label = Label(self, text="Points of interest")
        self.interest_points_label.grid(column=col+2, row=row, sticky=W, padx=5, pady=10)
        self.transport_label = Label(self, text="Transport Provider")
        self.transport_label.grid(column=col+3, row=row, sticky=W, padx=5, pady=10)
        self.transport_mode_label = Label(self, text="Transport Mode")
        self.transport_mode_label.grid(column=col+4, row=row, sticky=W, padx=5, pady=10)

        #Check if the trip has travellers, 4th element is the travellers list
        if self.trip_legs:
            
            for i, trip_leg in enumerate(self.trip_legs):

                starting_location = trip_leg.starting_location
                strat_location_entry = Label(self, text=starting_location)
                strat_location_entry.grid(column=0, row=row+1+i, sticky=W, padx=10, pady=10)

                destination =  trip_leg.destination
                destination_entry = Label(self, text=destination)
                destination_entry.grid(column=1, row=row+1+i, sticky=W, padx=10, pady=10)

                points_of_interests = self.trip_legs[i].point_of_interest
                interest_points_label = Label(self, text=points_of_interests)
                interest_points_label.grid(column=2, row=row+1+i, sticky=W, padx=10, pady=10)

                transport_provider = self.trip_legs[i].transport_provider
                transport_label = Label(self, text=transport_provider)
                transport_label.grid(column=3, row=row+1+i, sticky=W, padx=10, pady=10)

                transport_mode = self.trip_legs[i].transport_mode
                transport_mode_label = Label(self, text=transport_mode)
                transport_mode_label.grid(column=4, row=row+1+i, sticky=W, padx=10, pady=10) 
                
                update_btn = Button(self, command=lambda: update_trip_leg(trip_leg) ,text='Update Trip Leg', bg = '#20bebe')
                update_btn.grid(column=5, row=row+1+i, sticky=W, padx=5, pady=10)

                del_btn = Button(self, command=lambda: delete_trip_leg(i) ,text='Delete Trip Leg', bg = 'red')
                del_btn.grid(column=col+6, row=row+1+i, sticky=W, padx=5, pady=10)
            

        else:
            messagebox.showinfo(title="No Trip Legs", message="No Trip Legs to display")
            



  
        

        # self.date_entry.insert("Date Format")    


