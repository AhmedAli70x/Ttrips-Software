

from datetime import datetime
from tkinter import *
from tkinter import ttk

from invoice import Invoice

class TakePaymentGUI(Tk):

    def __init__(self, system, trip_id):
        super().__init__()
        self.system = system
        self.trip_id = trip_id
   
        self.title("Take Payement")
        self.geometry("500x600")
        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 2)
        # self.configure(bg='white')
              
        self.take_payment = Label(self, text="Take Payment", bg="#20bebe")
        self.take_payment.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)

        def save_invoice():
            cur_user_name = self.username_var.get()
            date = self.date_var.get()
            trip_name = self.trip_name_var.get()
            amount = self.amount_entry.get()
            traveller = self.traveller_entry.get()

            new_invoice = Invoice(amount, trip_name, cur_user_name, traveller, date)
            print(new_invoice.number)

        col = 0
        row = 1


        self.username_label = Label(self, text="User Name: ")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_var= StringVar(self, value= self.system.cur_user.name)
        self.username_entry = Label(self, textvariable = self.username_var, bg="white")
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

         
        self.date_label = Label(self, text="Date: ")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar(self, value= datetime.today().strftime('%Y-%m-%d'))
        self.date_entry = Label(self, textvariable = self.date_var , bg="white")
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

            
        self.trip_name_label = Label(self, text="Trip Name: ")
        self.trip_name_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.trip_name_var= StringVar(self, value= self.system.trips[self.trip_id].name)
        self.trip_name_entry = Label(self, textvariable = self.trip_name_var , bg="white")
        self.trip_name_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.amount_label = Label(self, text="Amount: ")
        self.amount_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.amount_var= StringVar()
        self.amount_entry = Entry(self, textvariable = self.amount_var)
        self.amount_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 



        travellers_list = []
        for traveller in self.system.trips[self.trip_id].travellers:
            travellers_list.append(traveller.name)

        self.traveller_label = Label(self, text="Traveller: ")
        self.traveller_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)
        self.traveller_entry = ttk.Combobox(self, values = travellers_list)
        self.traveller_entry.current(0)
        self.traveller_entry.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10) 



        save_invoice_btn = Button(self, command= save_invoice ,text='Save', bg = '#20bebe')
        save_invoice_btn.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)


