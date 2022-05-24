from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk




class Trips(Tk):

    def __init__(self, system =None):
        super().__init__()
        self.system = system
        # set window attributes
        self.title("Trips")
        self.geometry("500x600")
        self.resizable(0, 0)
        # self.columnconfigure(0, weight= 1)
        # self.columnconfigure(1, weight= 3)


        # add components
        col =0
        row = 1

        self.menu = ttk.Notebook(self)
        self.menu.pack(pady= 15)

        self.create_trip = Frame(self.menu, width=500, height=500, bg="blue")
        self.view_trips = Frame(self.menu, width=500, height=500, bg="red")

        self.create_trip.pack(fill="both", expand=1)
        self.view_trips.pack(fill="both", expand=1)

        self.menu.add(self.create_trip, text="Create Trip")
        self.menu.add(self.view_trips, text="View Trip")




        def save_form():
            pass
            # name = self.name_entry.get()
            # date = self.date_entry.get()
            # dur = self.dur_entry.get()
            # print(name, date, dur)
            # new_trip = Trip(name, date, dur)
            # self.system.trips.append(new_trip)
            # print(self.system.trips)

        # self.submit_text= StringVar()
        # self.submit_btn = Button(self.create_trip, command= save_form ,textvariable= self.submit_text, bg = "#20bebe")
        # self.submit_text.set("Submit")
        # self.submit_btn.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

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

        
treip  = Trips()  
treip.mainloop()   

        # self.date_entry.insert("Date Format")    


