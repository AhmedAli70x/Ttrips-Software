from cgitb import text
import imp
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import traceback

from tk_view_trip_legs import ViewTripLegs
from tk_create_traveller import CreateTraveller
from tk_view_travellers import ViewTravellers
from tk_create_trip_leg import CreateTripLeg
from tk_take_payment import TakePaymentGUI


class CoodinatorMenu(Tk):
    def __init__(self, system):
        super().__init__()
        self.system = system

        for trip in self.system.trips:
            if trip.trip_coodinator == self.system.cur_user:
                self.trip = trip
                # print("Success")
                break
            


        self.title("Coodinator Menu")
        self.geometry("750x500")
        self.resizable(0, 0)

        self.head_label = Label(self, text="Trip System", bg="#20bebe")
        self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        self.menu = ttk.Notebook(self)
        self.menu.grid(column=0,row=0,padx=5, pady=10)

        self.create_trip = Frame(self.menu, width=700, height=500,  )
        self.view_trips = Frame(self.menu, width=700, height=500, bg='white')
        self.create_user = Frame(self.menu, width=700, height=500, bg='white')

        self.create_trip.pack(fill="both", expand=1)
        self.view_trips.pack(fill="both", expand=1)
        self.create_user.pack(fill="both", expand=1)
        
        self.menu.add(self.create_trip, text="Associated Trip")
        self.menu.add(self.view_trips, text="View Trip")
        self.menu.add(self.create_user, text="Create User")
        self.menu.forget(self.create_trip)
        self.menu.forget(self.create_user)




        col =0
        row =1

        
        def create_traveller():
            # print("My create id is", id)
            new_traveller = CreateTraveller(self.trip)
            new_traveller.mainloop()
            # print(f"Add Traveller Run {id}")

        def view_travellers():
            # print("id is", id, self.system.trips[id])
            trip_traveller = self.trip.travellers
            view_travellers = ViewTravellers(trip_traveller)
            view_travellers.mainloop()
            # print(self.system.trips[0].travellers)
            
        def create_trip_leg():
            trip_tip_leg = self.trip.trip_legs
            create_trip_leg  = CreateTripLeg(trip_tip_leg)
            create_trip_leg.mainloop()
        
        def view_trip_legs():
            trip_legs = self.trip.trip_legs
            gui_trip_legs = ViewTripLegs(trip_legs)
            gui_trip_legs.mainloop()

        

        def take_payment():
            take_payment = TakePaymentGUI(self.system, self.trip)

        self.name_view = Label(self.view_trips, text="Name")
        self.name_view.grid(column=col, row=row+1, sticky=E, padx=10, pady=10)
        self.date_view = Label(self.view_trips, text="Start Date")
        self.date_view.grid(column=col+1, row=row+1, sticky=E, padx=10, pady=10)
        self.duration_view = Label(self.view_trips, text="Duration")
        self.duration_view.grid(column=col+2, row=row+1, sticky=E, padx=10, pady=10)

        self.traveller_label = Label(self.view_trips, text="Create Traveller")
        self.traveller_label.grid(column=col+3, row=row+1, sticky=E, padx=10, pady=10)

        self.trip_leg_view = Label(self.view_trips, text="Create Trip Leg")
        self.trip_leg_view.grid(column=col+4, row=row+1, sticky=E, padx=10, pady=10)


        trip_name = self.trip.name
        name_view_label = Label(self.view_trips, text=trip_name)
        name_view_label.grid(column=0, row=row+2, sticky=E, padx=10, pady=10)

        start_date = self.trip.start_date
        name_view_label = Label(self.view_trips, text=start_date)
        name_view_label.grid(column=1, row=row+2, sticky=E, padx=10, pady=10)

        duration_name = self.trip.duration
        name_view_label = Label(self.view_trips, text=duration_name)
        name_view_label.grid(column=2, row=row+2, sticky=E, padx=10, pady=10)
                
        create_traveller_btn = Button(self.view_trips, command=lambda: create_traveller() ,text='Create Traveller', bg = '#20bebe')
        create_traveller_btn.grid(column=col+3, row=row+2, sticky=W, padx=5, pady=10)

        create_trip_leg_btn = Button(self.view_trips, command=lambda: create_trip_leg() ,text='Create Trip Leg', bg = '#20bebe')
        create_trip_leg_btn.grid(column=col+4, row=row+2, sticky=W, padx=5, pady=10)

        view_travellers_btn =Button(self.view_trips, command=lambda: view_travellers() ,text='View Travellers', bg = '#20bebe')
        view_travellers_btn.grid(column=col+5, row=row+2, sticky=W, padx=5, pady=10)

        view_trip_legs_btn = Button(self.view_trips, command=lambda: view_trip_legs() ,text='View Trip Legs', bg = '#20bebe')
        view_trip_legs_btn.grid(column=col+6, row=row+2, sticky=W, padx=5, pady=10)

        take_payment_btn = Button(self.view_trips, command=lambda: take_payment() ,text='Take Payment', bg = 'magenta')
        take_payment_btn.grid(column=col+7, row=row+2, sticky=W, padx=5, pady=10)

