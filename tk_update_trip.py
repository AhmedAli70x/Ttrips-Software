
from cProfile import label
from tkinter import *
from tkinter import ttk
import traceback
from tkinter import messagebox


class UpdateTrip(Tk):
    def __init__(self, system,  trip):
        super().__init__()
        self.system = system
        self.trip = trip

        self.title("Update Trip")
        self.geometry("500x500")

        self.head_label = Label(self, text="Update Trip", bg="#20bebe")
        self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        col =0
        row =1

        def update_trip():
            try:
                name = self.name_entry.get()
                date = self.date_entry.get()
                dur = self.dur_entry.get()
                coodinator_entry = self.coodinator_entry.get()
                manager_entry = self.manager_entry.get()

                if coodinator_entry:
                    coo_class = self.system.search_user(coodinator_entry)
                    self.trip.trip_coodinator = coo_class

                if manager_entry:
                    man_class = self.system.search_user(manager_entry)
                    self.trip.trip_manager = man_class

                suppot_entry = self.suppot_entry.get()
                self.trip.name = name
                self.trip.start_date = date
                self.trip.duration = dur

                if self.trip.support_staff_num:
                    self.trip.add_support_staff(suppot_entry)

                messagebox.showinfo(title="Success", message="Trip Update Successfully",)
                self.destroy()
            except Exception:
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
        self.dur_entry = ttk.Combobox(self, values=["one_day", "weekend", "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.coodinator_label = Label(self, text="Trip Coodinator: ")
        self.coodinator_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)
        self.coodinator_var = StringVar(self, value= self.trip.coodinator)
        self.coodinator_entry = ttk.Combobox(self, textvariable= self.coodinator_var, values= self.system.system_coodinators)
        self.coodinator_entry.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10)  

        self.contact_label = Label(self, text="Coodinator Contact: ")
        self.contact_label.grid(column=col, row=row+5, sticky=E, padx=5, pady=10)
        if self.trip.contact:
            self.contact_entry = Label(self, text= self.trip.contact)
            self.contact_entry.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)
        else:
            self.contact_entry = Label(self, text= "NA")
            self.contact_entry.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)


        self.manager_label = Label(self, text="Trip Manager: ")
        self.manager_label.grid(column=col, row=row+6, sticky=E, padx=5, pady=10)
        self.manager_var = StringVar(self, value= self.trip.manager)
        self.manager_entry = ttk.Combobox(self, textvariable= self.manager_var, values= self.system.system_managers)
        self.manager_entry.grid(column=col+1, row=row+6, sticky=W, padx=5, pady=10)  


        self.support_label = Label(self, text=f"Support Staff {self.trip.support_staff_num}: ")
        self.support_label.grid(column=col, row=row+7, sticky=E, padx=5, pady=10)
        if self.trip.support_staff_num:
            for num in self.trip.support_staff_num:
                self.support_var= StringVar(self)
                self.suppot_entry = Entry(self, textvariable = self.support_var)
                self.suppot_entry.grid(column=col+1+num, row=row+7, sticky=W, padx=5, pady=10) 
        else:

            self.suppot_entry = Entry(self, text = "NA")
            self.suppot_entry.grid(column=col+1, row=row+7, sticky=W, padx=5, pady=10) 
            self.suppot_entry.config(state= "disabled")

        self.submit_btn = Button(self, command= update_trip ,text= "Save", bg = "#20bebe")
        self.submit_btn.grid(column=col+1, row=row+8, sticky=W, padx=5, pady=10)
        