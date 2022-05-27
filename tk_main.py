from cgitb import text
import imp
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import traceback
from tk_update_traveller import UpdateTraveller
from tk_view_trip_legs import ViewTripLegs

from trips import Trip
from tk_create_traveller import CreateTraveller
from tk_view_travellers import ViewTravellers
from tk_create_trip_leg import CreateTripLeg
from tk_update_trip import UpdateTrip
from users import * 

class MainMenu(Tk):
    def __init__(self, system):
        super().__init__()
        self.system = system
        self.title("Trips")
        self.geometry("800x500")


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

        self.menu.add(self.create_trip, text="Create Trip")
        self.menu.add(self.view_trips, text="View Trip")
        self.menu.add(self.create_user, text="Create User")

        col =0
        row =1

        def save_trip():
            try:
                name = self.name_entry.get()
                date = self.date_entry.get()
                dur = self.dur_entry.get()
                # print(dur)
                new_trip = Trip(name, date, duration=dur)
                self.system.trips.append(new_trip)
                messagebox.showinfo(title="Success", message="Trip Created Successfully",)
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showerror(title="Error", message="Fail to create new trip",)

        self.name_label = Label(self.create_trip, text="Name:")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var= StringVar()
        self.name_entry = Entry(self.create_trip, textvariable = self.name_var)
        self.name_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.date_label = Label(self.create_trip, text="Start Date:")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar()
        self.date_entry = Entry(self.create_trip, textvariable = self.date_var)
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.dur_label = Label(self.create_trip, text="Duration:")
        self.dur_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.dur_var = StringVar()
        self.dur_entry = ttk.Combobox(self.create_trip, textvariable=self.dur_var, values=["one_day", "weekend", "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10)  

        self.submit_btn = Button(self.create_trip, command= save_trip ,text= "Save", bg = "#20bebe")
        self.submit_btn.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 

        
        def create_traveller(id):
            # print("My create id is", id)
            new_traveller = CreateTraveller(self.system, id)
            new_traveller.mainloop()
            # print(f"Add Traveller Run {id}")

        def view_travellers(id):
            # print("id is", id, self.system.trips[id])
            trip_traveller = self.system.trips[id].travellers
            view_travellers = ViewTravellers(trip_traveller)
            view_travellers.mainloop()
            # print(self.system.trips[0].travellers)
            
        def create_trip_leg(id):
            trip_tip_leg = self.system.trips[id].trip_legs
            create_trip_leg  = CreateTripLeg(trip_tip_leg)

        
        def view_trip_legs(id):
            trip_legs = self.system.trips[id].trip_legs
            gui_trip_legs = ViewTripLegs(trip_legs)
            gui_trip_legs.mainloop()
  
        def delete_trip(id):
            self.system.trips.pop(id)
            self.destroy()
            self.__init__(self.system)

        
        def update_trip(id):
            update_trip = UpdateTrip(self.system.trips[id])


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

        def view_trips(event):
            trips_numer = len(self.system.trips)
            if trips_numer:
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
                            
                    create_traveller_btn = Button(self.view_trips, command=lambda: create_traveller(i) ,text='Create Traveller', bg = '#20bebe')
                    create_traveller_btn.grid(column=col+3, row=row+6+i, sticky=W, padx=5, pady=10)

                    create_trip_leg_btn = Button(self.view_trips, command=lambda: create_trip_leg(i) ,text='Create Trip Leg', bg = '#20bebe')
                    create_trip_leg_btn.grid(column=col+4, row=row+6+i, sticky=W, padx=5, pady=10)

                    view_travellers_btn =Button(self.view_trips, command=lambda: view_travellers(i) ,text='View Travellers', bg = '#20bebe')
                    view_travellers_btn.grid(column=col+5, row=row+6+i, sticky=W, padx=5, pady=10)

                    view_trip_legs_btn = Button(self.view_trips, command=lambda: view_trip_legs(i) ,text='View Trip Legs', bg = '#20bebe')
                    view_trip_legs_btn.grid(column=col+6, row=row+6+i, sticky=W, padx=5, pady=10)

                    update_trip_btn = Button(self.view_trips, command=lambda: update_trip(i), text = "Update Trip", bg="yellow")
                    update_trip_btn.grid(column= col+7, row=row+6+i, sticky=W, padx=5, pady=10)

                    delete_trip_btn = Button(self.view_trips, command=lambda: delete_trip(i) ,text='Delete', bg = 'red')
                    delete_trip_btn.grid(column=col+8, row=row+6+i, sticky=W, padx=5, pady=10)





        def create_user():
            username = self.username_entry.get()
            password = self.password_entry.get()
            phone = self.phone_entry.get()
            role = self.role_entry.get()
            print(f"Create New User ")
            if role == "Coodinator":
                new_user = Coodinator(username, password, phone)
            elif role == "Manager":
                new_user = Manager(username, password, phone)
            elif role == "Administrator":
                new_user = Administrator(username, password, phone)
            self.system.users.append(new_user)
            messagebox.showinfo( title="Success", message=f"User Created Successfully")
        

        self.username_label = Label(self.create_user, text="Username: ")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_entry = Entry(self.create_user)
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.password_label = Label(self.create_user, text="Password: ")
        self.password_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.password_entry = Entry(self.create_user)
        self.password_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.phone_label = Label(self.create_user, text="Phone: ")
        self.phone_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.phone_entry = Entry(self.create_user)
        self.phone_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.role_label = Label(self.create_user, text="Role: ")
        self.role_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.role_entry = ttk.Combobox(self.create_user, values=["Coodinator", "Manager",  "Administrator"])
        self.role_entry.current(0)
        self.role_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  
            
        self.create_user_btn = Button(self.create_user, command= create_user ,text= "Save", bg = "#20bebe")
        self.create_user_btn.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10)

        self.menu.bind('<<NotebookTabChanged>>',view_trips)

        # def view_users(event):
        #     pass
        # self.menu.bind('<<NotebookTabChanged>>',view_users)


