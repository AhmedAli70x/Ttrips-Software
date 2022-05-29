
from tkinter import *
from tkinter import ttk
import traceback
from tkinter import messagebox


class UpdateTrip(Tk):
    def __init__(self, trip):
        super().__init__()
        self.trip = trip

        self.title("Update Trip")
        self.geometry("800x500")

        self.head_label = Label(self, text="Update Trip", bg="#20bebe")
        self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        col =0
        row =1

        def update_trip():
            try:
                name = self.name_entry.get()
                date = self.date_entry.get()
                dur = self.dur_entry.get()
                self.trip.name = name
                self.trip.start_date = date
                self.trip.duration = dur
                messagebox.showinfo(title="Success", message="Trip Update Successfully",)
            except ZeroDivisionError:
                traceback.print_exc()
                messagebox.showerror(title="Error", message="Fail to Update trip",)

        self.name_label = Label(self, text="Name:")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var= StringVar(self, value=self.trip.name)
        self.name_entry = Entry(self, textvariable = self.name_var)
        self.name_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.date_label = Label(self, text="Start Date:")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar(self, value=self.trip.start_date)
        self.date_entry = Entry(self, textvariable = self.date_var)
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.dur_label = Label(self, text="Duration:")
        self.dur_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.dur_var = StringVar(self, value=self.trip.duration)
        self.dur_entry = ttk.Combobox(self, textvariable=self.dur_var, values=["one_day", "weekend", "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 

        self.contact_label = Label(self, text="Contact:")
        self.contact_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.contact_var= StringVar(self, value=self.trip.contact_numer)
        self.contact_entry = Entry(self, textvariable = self.contact_var)
        self.contact_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.support_label = Label(self, text="Support Staff:")
        self.support_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.support_var= StringVar(self, value=self.trip.contact_numer)
        self.suppot_entry = Entry(self, textvariable = self.support_var)
        self.suppot_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        self.submit_btn = Button(self, command= update_trip ,text= "Save", bg = "#20bebe")
        self.submit_btn.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)
        