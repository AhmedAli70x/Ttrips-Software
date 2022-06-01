

from tkinter import Tk
from tkinter import messagebox
import traceback
from datetime import datetime

from tkinter import *
from invoice import Invoice 
from validation import Validation as v


class TripTotalGUI(Tk):

    def __init__(self, system, trip):
        super().__init__()
        self.system = system
        self.trip = trip
          
        self.title("Trip Total Payment")
        self.geometry("500x600")
        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 2)   
        self.take_payment = Label(self, text="Trip Total Payment", bg="#20bebe")
        self.take_payment.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)

        def print_invoice():

            try:
                amount = self.amount_var.get()
                trip_name = self.trip_name_var.get()
                cur_user_name = self.username_var.get()
                date = self.date_var.get()

                check_invoice = v.check_invoice(amount, traveller="NO Traveller")
                if check_invoice:
                        new_invoice = Invoice(float(amount), trip_name, cur_user_name, traveller="NO Traveller", date=date)
                        self.system.trip_tot_invoices.append(new_invoice)
                        print()
                        print(' Generating Invoice.....:')
                        print(' Invoice Details:')
                        print(' Invoice Trip:', trip_name)
                        print(' Invoice Amount:', amount)
                        print(' Invoice Username:', cur_user_name)
                        print(" Invoice Date:", date)
                        print()

                        self.destroy()
                        messagebox.showinfo(title="Success", message="Payment Received",)

            except Exception:
                traceback.print_exc()
                messagebox.showerror(title="Error", message="Payment Fail",)



        col = 0
        row = 1


        self.username_label = Label(self, text="Name: ")
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
        self.trip_name_var= StringVar(self, value= self.trip.name)
        self.trip_name_entry = Label(self, textvariable = self.trip_name_var , bg="white")
        self.trip_name_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.amount_label = Label(self, text="Total Trip Payments: ")
        self.amount_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.amount_var= StringVar(self, value= self.trip.total_invoice)
        self.amount_entry = Label(self, textvariable = self.amount_var, bg="yellow")
        self.amount_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 

        save_invoice_btn = Button(self, command= print_invoice ,text='Print Invoice', bg = '#20bebe')
        save_invoice_btn.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)



