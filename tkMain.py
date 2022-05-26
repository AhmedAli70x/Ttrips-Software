from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import traceback
from tkUpdateTraveller import UpdateTraveller

from trips import Trip
from tkTrips import Trips
from functools import partial
from tkCreateTraveller import CreateTraveller
from tkViewTravellers import ViewTravellers

class MainMenu(Tk):
    def __init__(self, system):
        super().__init__()
        self.system = system
        print(system.trips)
        # set window attributes
        self.title("Trips")
        self.geometry("700x500")
        self.resizable(0, 0)
        # self.columnconfigure(0, weight= 1)
        # self.columnconfigure(1, weight= 1)
        self.head_label = Label(self, text="Trip System", bg="#20bebe")
        self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        self.menu = ttk.Notebook(self)
        self.menu.grid(column=0,row=0,padx=5, pady=10)

        self.create_trip = Frame(self.menu, width=700, height=500,  )
        self.view_trips = Frame(self.menu, width=700, height=500, bg='white')

        self.create_trip.pack(fill="both", expand=1)
        self.view_trips.pack(fill="both", expand=1)

        self.menu.add(self.create_trip, text="Create Trip")
        self.menu.add(self.view_trips, text="View Trip")


        # add components
        col =0
        row =1
        self.name_label = Label(self.create_trip, text="Name:")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var= StringVar()
        self.name_entry = Entry(self.create_trip, textvariable = self.name_var)
        # self.name_var.set(self.system.trips[0])
        self.name_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.date_label = Label(self.create_trip, text="Start Date:")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar()
        self.date_entry = Entry(self.create_trip, textvariable = self.date_var)
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.dur_label = Label(self.create_trip, text="Duration:")
        self.dur_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.dur_entry = ttk.Combobox(self.create_trip, values=["one_day", "weekend",  "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10)  

        def save_form():
            try:
                name = self.name_entry.get()
                date = self.date_entry.get()
                dur = self.dur_entry.get()
                print(name, date, dur)
                new_trip = Trip(name, date, dur)
                self.system.trips.append(new_trip)
                messagebox.showinfo(title=None, message="Trip Created Successfully",)
                view_trips()
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showinfo(title=None, message="Fail to create new trip",)
        self.submit_text= StringVar()
        self.submit_btn = Button(self.create_trip, command= save_form ,textvariable= self.submit_text, bg = "#20bebe")
        self.submit_text.set("Save")
        self.submit_btn.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 

        
        def create_traveller(id):
            # print("My create id is", id)
            new_traveller = CreateTraveller(self.system, id)
            new_traveller.mainloop()
            # print(f"Add Traveller Run {id}")

        def view_travellers(id):
            print("id is", id, self.system.trips[id])
            view_travellers = ViewTravellers(self.system, id)
            view_travellers.mainloop()
            # print(self.system.trips[0].travellers)
            
        def create_trip_leg(id):
            print(f"Add Traveller Run {id}")
            update_traveller = UpdateTraveller()
            

        self.name_view = Label(self.view_trips, text="Name")
        self.name_view.grid(column=col, row=row+5, sticky=E, padx=10, pady=10)
        self.date_view = Label(self.view_trips, text="Start Date")
        self.date_view.grid(column=col+1, row=row+5, sticky=E, padx=10, pady=10)
        self.duration_view = Label(self.view_trips, text="Duration")
        self.duration_view.grid(column=col+2, row=row+5, sticky=E, padx=10, pady=10)

        self.traveller_label = Label(self.view_trips, text="Create Traveller")
        self.traveller_label.grid(column=col+2, row=row+5, sticky=E, padx=10, pady=10)

        self.trip_leg_view = Label(self.view_trips, text="Create Trip Leg")
        self.trip_leg_view.grid(column=col+2, row=row+5, sticky=E, padx=10, pady=10)

        

        def view_trips(*args):
            buttons = []
            buttons2 = []
            buttons3 = []
            trips_numer = len(self.system.trips)
            for i in range(trips_numer):
                trip_name = self.system.trips[i].name
                name_view_label = Label(self.view_trips, text=trip_name)
                name_view_label.grid(column=0, row=row+6+i, sticky=E, padx=10, pady=10)

                start_date = self.system.trips[i].start_date
                name_view_label = Label(self.view_trips, text=start_date)
                name_view_label.grid(column=1, row=row+6+i, sticky=E, padx=10, pady=10)

                duration_name = self.system.trips[i].duration
                name_view_label = Label(self.view_trips, text=duration_name)
                name_view_label.grid(column=2, row=row+6+i, sticky=E, padx=10, pady=10)
                
              
                buttons.append(Button(self.view_trips, command=lambda: create_traveller(i) ,text='Add Traveller', bg = '#20bebe'))
                buttons[i].grid(column=col+3, row=row+6+i, sticky=W, padx=5, pady=10)

                buttons2.append(Button(self.view_trips, command=lambda: create_trip_leg(i) ,text='Add Trip Leg', bg = '#20bebe'))
                buttons2[i].grid(column=col+4, row=row+6+i, sticky=W, padx=5, pady=10)

                buttons3.append(Button(self.view_trips, command=lambda: view_travellers(i) ,text='View Travellers', bg = '#20bebe'))
                buttons3[i].grid(column=col+5, row=row+6+i, sticky=W, padx=5, pady=10)

        self.menu.bind('<<NotebookTabChanged>>',view_trips)
        



