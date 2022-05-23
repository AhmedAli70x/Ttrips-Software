from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
from trips import Trip


class Trips(Tk):

    def __init__(self):
        super().__init__()
        # set window attributes
        self.title("Trips")
        self.geometry("500x600")
        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 3)
        
        # add components
        col =0
        row = 0

        


        self.name_label = Label(self, text="Name:")
        self.name_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.name_var= StringVar()
        self.name_entry = Entry(self, textvariable = self.name_var)
        self.name_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.date_label = Label(self, text="Start Date:")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar()
        self.date_entry = Entry(self, textvariable = self.date_var)
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.dur_label = Label(self, text="Duration:")
        self.dur_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.dur_var= StringVar()
        self.dur_entry = ttk.Combobox(self, values=[ "one_day", "weekend",  "fortnight"])
        self.dur_entry.current(0)
        self.dur_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10)  

        def save_form():
            name = self.name_entry.get()
            date = self.date_var.get()
            dur = self.dur_entry.get()
            print(name, date, dur)
            # new_trip = Trip(name, date, dur)

            # print("Tkinter is easy to use!")

        self.submit_text= StringVar()
        self.submit_btn = Button(self, command= save_form ,textvariable= self.submit_text, bg = "#20bebe")
        self.submit_text.set("Submit")
        self.submit_btn.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  

        
        

        # self.date_entry.insert("Date Format")    


if __name__ == "__main__":
    gui = Trips()
    gui.mainloop()