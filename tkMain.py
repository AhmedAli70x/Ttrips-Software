from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from trips import Trip
from tkTrips import Trips


global col
global row
class MainMenu(Tk):

    def __init__(self, system):
        super().__init__()
        self.system = system
        # set window attributes
        self.title("Trips")
        self.geometry("500x600")
        self.resizable(0, 0)
        # self.columnconfigure(0, weight= 1)
        # self.columnconfigure(1, weight= 1)
        # self.head_label = Label(text="System Features", bg="#20bebe")
        # self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        self.menu = ttk.Notebook(self)
        self.menu.pack(pady= 15)

        self.create_trip = Frame(self.menu, width=500, height=500,  )
        self.view_trips = Frame(self.menu, width=500, height=500, bg='white')

        # self.create_trip.pack(fill="both", expand=1)
        # self.view_trips.pack(fill="both", expand=1)

        self.menu.add(self.create_trip, text="Create Trip")
        self.menu.add(self.view_trips, text="View Trip")


        # add components
        col =0
        row = 0



        def save_form():
            name = self.name_entry.get()
            date = self.date_entry.get()
            dur = self.dur_entry.get()
            print(name, date, dur)
            new_trip = Trip(name, date, dur)
            self.system.trips.append(new_trip)
            print(self.system.trips)


        col =0
        row = 1

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
        self.dur_var= StringVar()
        self.dur_entry = ttk.Combobox(self.create_trip, values=[ "one_day", "weekend",  "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10)  

        def save_form():
            name = self.name_entry.get()
            date = self.date_entry.get()
            dur = self.dur_entry.get()
            # print(name, date, dur)
            new_trip = Trip(name, date, dur)
            self.system.trips.append(new_trip)
            # print(self.system.trips)
            view_trips()

        self.submit_text= StringVar()
        self.submit_btn = Button(self.create_trip, command= save_form ,textvariable= self.submit_text, bg = "#20bebe")
        self.submit_text.set("Save")
        self.submit_btn.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 


        def add_traveller(id):

            pass

        self.name_view = Label(self.create_trip, text="Name")
        self.name_view.grid(column=col, row=row+5, sticky=E, padx=10, pady=10)
        self.date_view = Label(self.create_trip, text="Start Date")
        self.date_view.grid(column=col+1, row=row+5, sticky=E, padx=10, pady=10)
        self.duration_view = Label(self.create_trip, text="Duration")
        self.duration_view.grid(column=col+2, row=row+5, sticky=E, padx=10, pady=10)

        def view_trips(*args):
            for trip in self.system.trips:
                print(trip.id)
                print(trip.name)

                exec(f"name_view_label{trip.id} = Label(self.create_trip, text=trip.name)")  
                exec(f"name_view_label{trip.id}.grid(column=0, row=6+trip.id, sticky=E, padx=10, pady=10)")  

                exec(f"date_view_label{trip.id} = Label(self.create_trip, text=trip.start_date)")
                exec(f"date_view_label{trip.id}.grid(column=1, row=6+trip.id, sticky=E, padx=10, pady=10)")

                exec(f"dur_view_label{trip.id} = Label(self.create_trip, text=trip.duration)")
                exec(f"dur_view_label{trip.id}.grid(column=2, row=6+trip.id, sticky=E, padx=10, pady=10)")

                exec(f"dur_view_btn{trip.id} = Label(self.create_trip, text=trip.duration)")
                exec(f"dur_view_btn{trip.id}.grid(column=2, row=6+trip.id, sticky=E, padx=10, pady=10)")

                self.submit_text= StringVar()
                self.submit_btn = Button(self.create_trip, command=lambda: add_traveller({trip.id}) ,textvariable= self.submit_text, bg = "#20bebe")
                self.submit_text.set("Add Traveller")
                self.submit_btn.grid(column=col+3, row=row+6, sticky=W, padx=5, pady=10) 

        self.menu.bind('<<NotebookTabChanged>>',view_trips)
        

        # self.create_trip= StringVar()
        # self.create_trip_btn = Button(self, command= ceate_trip ,textvariable= self.create_trip, bg = "#20bebe")
        # self.create_trip_btn.grid(column=col, row=row+1, sticky=W, padx=5, pady=10)  
        # self.create_trip.set("Create Trip")

        # self.view_trips= StringVar()
        # self.view_trips_btn = Button(self, command= view_trips ,textvariable= self.view_trips, bg = "#20bebe")
        # self.view_trips_btn.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10)  
        # self.view_trips.set("View Trips")

        # self.date_entry.insert("Date Format")    


