

from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import traceback
from invoice import Invoice
from validation import Validation as v


class UpdateInvoice(Tk):

    def __init__(self, invoice):
        super().__init__()
        self.invoice = invoice
   
        self.title("Update Invoice")
        self.geometry("500x600")
        self.resizable(0, 0)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 2)
        # self.configure(bg='white')
              
        self.take_payment = Label(self, text="Update Invoice", bg="#20bebe")
        self.take_payment.grid( column= 1 , row=0, sticky=W, padx=10, pady=10)

        def update_invoice():
            try:
                try:
                    amount = self.amount_entry.get()               
                    trip_name = self.trip_name_var.get()
                    user_name = self.username_var.get()
                    traveller = self.traveller_entry.get()
                    date = self.date_var.get()

                    check_invoice = v.check_invoice(amount, traveller)
                    if check_invoice:

                        self.invoice.name = user_name
                        self.invoice.date = date
                        self.invoice.trip = trip_name
                        self.invoice.amount = float(amount)
                        self.invoice.traveller_name = traveller
                        self.destroy()
                        messagebox.showinfo(title="Success", message="Invoice Updated")

                except ValueError:
                    messagebox.showerror(title="Error", message="Please enter a valid amount",)


            except Exception:
                traceback.print_exc()
                messagebox.showinfo(title="Fail", message="Process fail",)

            

        col = 0
        row = 1



        self.username_label = Label(self, text="User Name: ")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_var= StringVar(self, value= self.invoice.username)
        self.username_entry = Label(self, textvariable = self.username_var, bg="white")
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10) 

         
        self.date_label = Label(self, text="Date: ")
        self.date_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.date_var= StringVar(self, value= self.invoice.date)
        self.date_entry = Label(self, textvariable = self.date_var , bg="white")
        self.date_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

            
        self.trip_name_label = Label(self, text="Trip Name: ")
        self.trip_name_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.trip_name_var= StringVar(self, value= self.invoice.trip)
        self.trip_name_entry = Label(self, textvariable = self.trip_name_var , bg="white")
        self.trip_name_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.amount_label = Label(self, text="Amount: ")
        self.amount_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.amount_var= StringVar(self, value= self.invoice.amount)
        self.amount_entry = Entry(self, textvariable = self.amount_var)
        self.amount_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10) 

        self.traveller_label = Label(self, text="Traveller: ")
        self.traveller_label.grid(column=col, row=row+4, sticky=E, padx=5, pady=10)

     

        self.traveller_var = StringVar(self, value=self.invoice.traveller_name)
        self.traveller_entry = ttk.Combobox(self, textvariable=self.traveller_var )
        self.traveller_entry.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10) 

        
        save_invoice_btn = Button(self, command= update_invoice ,text='Update', bg = '#20bebe')
        save_invoice_btn.grid(column=col+1, row=row+5, sticky=W, padx=5, pady=10)

  






            


