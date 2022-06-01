from cProfile import label
from cgitb import text
import imp
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import traceback
from invoice import Invoice
from tk_update_traveller import UpdateTraveller
from tk_view_trip_legs import ViewTripLegs

from trips import Trip
from tk_create_traveller import CreateTraveller
from tk_view_travellers import ViewTravellers
from tk_create_trip_leg import CreateTripLeg
from tk_update_trip import UpdateTrip
from tk_take_payment import TakePaymentGUI
from trip_total_payment import TripTotalGUI
from tk_update_user import UpdateUser
from tk_update_invoice import UpdateInvoice
from users import * 
from validation import Validation as v

class MainMenu(Tk):
    def __init__(self, system):
        super().__init__()
        self.system = system
        self.title("Trips System (Administrator)")
        self.geometry("1000x500")
        self.resizable(0, 0)


        self.head_label = Label(self, text="Trips System (Administrator)", bg="#20bebe")
        self.head_label.grid( column= 0 , row=0, sticky=W, padx=10, pady=10)

        self.menu = ttk.Notebook(self)
        self.menu.grid(column=0,row=0,padx=5, pady=10)

        self.create_trip = Frame(self.menu, width=700, height=500,  )
        self.view_trips = Frame(self.menu, width=700, height=500, bg='white')
        self.create_user = Frame(self.menu, width=700, height=500, bg='white')
        self.view_coodinators = Frame(self.menu, width=700, height=500, bg='white')
        self.view_managers = Frame(self.menu, width=700, height=500, bg='white')
        self.view_invoices = Frame(self.menu, width=700, height=500)
        self.view_total_invoices = Frame(self.menu, width=700, height=500, bg='white')

        self.create_trip.pack(fill="both", expand=1)
        self.view_trips.pack(fill="both", expand=1)
        self.create_user.pack(fill="both", expand=1)
        self.view_coodinators.pack(fill="both", expand=1)
        self.view_managers.pack(fill="both", expand=1)
        self.view_invoices.pack(fill="both", expand=1)
        self.view_total_invoices.pack(fill="both", expand=1)

        self.menu.add(self.create_trip, text="Create Trip")
        self.menu.add(self.view_trips, text="View Trip")
        self.menu.add(self.create_user, text="Create User")
        self.menu.add(self.view_coodinators, text="View Coodinators & Managers")
        self.menu.add(self.view_managers, text="View Managers")
        self.menu.forget(self.view_managers)

        self.menu.add(self.view_invoices, text="View Invoices")
        self.menu.add(self.view_total_invoices, text="View Total Invoices")

        col =0
        row =1

        def save_trip():
            try:
                name = self.name_entry.get()
                date = self.date_entry.get()
                dur = self.dur_entry.get()

                check_trip = v.check_trip(name, date)
                if check_trip:
                    new_trip = Trip(name, date, duration=dur)
                    self.system.trips.append(new_trip)
                    messagebox.showinfo(title="Success", message="Trip Created Successfully",)

            except Exception:
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

        
        def create_traveller(trip):
            # print("My create id is", id)
            new_traveller = CreateTraveller(trip)
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
            create_trip_leg.mainloop()

        
        def view_trip_legs(id):
            trip_legs = self.system.trips[id].trip_legs
            gui_trip_legs = ViewTripLegs(trip_legs)
            gui_trip_legs.mainloop()
  
        def delete_trip(id):
            self.system.trips.pop(id)
            self.destroy()
            self.__init__(self.system)

        
        def update_trip(id):
            update_trip = UpdateTrip(self.system, self.system.trips[id])
            update_trip.mainloop()

        def take_payment(trip):
            take_payment = TakePaymentGUI(self.system, trip)
            take_payment.mainloop()

        def gen_trip_invoice(trip):
            trip_total = TripTotalGUI(self.system, trip)
            trip_total.mainloop()

        self.name_view = Label(self.view_trips, text="Name")
        self.name_view.grid(column=col, row=row+1, sticky=E, padx=10, pady=10)
        self.date_view = Label(self.view_trips, text="Start Date")
        self.date_view.grid(column=col+1, row=row+1, sticky=E, padx=10, pady=10)
        self.duration_view = Label(self.view_trips, text="Duration")
        self.duration_view.grid(column=col+2, row=row+1, sticky=E, padx=10, pady=10)

        self.traveller_label = Label(self.view_trips, text="Create Traveller")
        self.traveller_label.grid(column=col+3, row=row+1, sticky=E, padx=10, pady=10)

        self.trip_leg_view = Label(self.view_trips, text="Create Trip Leg")
        self.trip_leg_view.grid(column=col+4, row=row+1, sticky=E, padx=10, pady=10)

        def view_trips(event):
            trips_numer = len(self.system.trips)
            if trips_numer:
                for i, trip in enumerate(self.system.trips):
                    trip_name = self.system.trips[i].name
                    name_view_label = Label(self.view_trips, text=trip_name)
                    name_view_label.grid(column=0, row=row+2+i, sticky=E, padx=10, pady=10)

                    start_date = self.system.trips[i].start_date
                    name_view_label = Label(self.view_trips, text=start_date)
                    name_view_label.grid(column=1, row=row+2+i, sticky=E, padx=10, pady=10)

                    duration_name = self.system.trips[i].duration
                    name_view_label = Label(self.view_trips, text=duration_name)
                    name_view_label.grid(column=2, row=row+2+i, sticky=E, padx=10, pady=10)
                            
                    create_traveller_btn = Button(self.view_trips, command=lambda: create_traveller(trip) ,text='Create Traveller', bg = '#20bebe')
                    create_traveller_btn.grid(column=col+3, row=row+2+i, sticky=W, padx=5, pady=10)

                    create_trip_leg_btn = Button(self.view_trips, command=lambda: create_trip_leg(i) ,text='Create Trip Leg', bg = '#20bebe')
                    create_trip_leg_btn.grid(column=col+4, row=row+2+i, sticky=W, padx=5, pady=10)

                    view_travellers_btn =Button(self.view_trips, command=lambda: view_travellers(i) ,text='View Travellers', bg = '#20bebe')
                    view_travellers_btn.grid(column=col+5, row=row+2+i, sticky=W, padx=5, pady=10)

                    view_trip_legs_btn = Button(self.view_trips, command=lambda: view_trip_legs(i) ,text='View Trip Legs', bg = '#20bebe')
                    view_trip_legs_btn.grid(column=col+6, row=row+2+i, sticky=W, padx=5, pady=10)

                    take_payment_btn = Button(self.view_trips, command=lambda: take_payment(trip) ,text='Take Payment', bg = 'magenta')
                    take_payment_btn.grid(column=col+7, row=row+2+i, sticky=W, padx=5, pady=10)


                    update_trip_btn = Button(self.view_trips, command=lambda: update_trip(i), text = "Update Trip", bg="yellow")
                    update_trip_btn.grid(column= col+8, row=row+2+i, sticky=W, padx=5, pady=10)

                    delete_trip_btn = Button(self.view_trips, command=lambda: delete_trip(i) ,text='Delete', bg = 'red')
                    delete_trip_btn.grid(column=col+9, row=row+2+i, sticky=W, padx=5, pady=10)

                    total_invoice_btn = Button(self.view_trips, command=lambda: gen_trip_invoice(trip) ,text='Tot Trip Invoice', bg = 'black', fg='white')
                    total_invoice_btn.grid(column=col+10, row=row+2+i, sticky=W, padx=5, pady=10)

        self.menu.bind('<<NotebookTabChanged>>', view_trips, add='+')


        def create_user():
            try:
                    
                username = self.username_entry.get()
                user_name = self.user_name_entry.get()
                phone = self.phone_entry.get()
                role = self.role_entry.get()
                #Validate user entries
                check_user = v.check_user(username, user_name, phone)
                if check_user:
                    if role == "c":
                        new_user = Coodinator(username, user_name, phone)
                    elif role == "m":
                        new_user = Manager(username,user_name,  phone)
                    elif role == "a":
                        new_user = Administrator(username,user_name,  phone)
                    self.system.users.append(new_user)
                    messagebox.showinfo( title="Success", message=f"User Created Successfully")
            except Exception:
                traceback.print_exc()
                messagebox.showerror(title="Error", message=f"User Create Error")


        self.username_label = Label(self.create_user, text="Username: ")
        self.username_label.grid(column=col, row=row, sticky=E, padx=5, pady=10)
        self.username_entry = Entry(self.create_user)
        self.username_entry.grid(column=col+1, row=row, sticky=W, padx=5, pady=10)     
           
        self.user_name_label = Label(self.create_user, text="Name: ")
        self.user_name_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        self.user_name_entry = Entry(self.create_user)
        self.user_name_entry.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=10) 

        self.phone_label = Label(self.create_user, text="Phone: ")
        self.phone_label.grid(column=col, row=row+2, sticky=E, padx=5, pady=10)
        self.phone_entry = Entry(self.create_user)
        self.phone_entry.grid(column=col+1, row=row+2, sticky=W, padx=5, pady=10) 


        self.role_label = Label(self.create_user, text="Role: ")
        self.role_label.grid(column=col, row=row+3, sticky=E, padx=5, pady=10)
        self.role_entry = ttk.Combobox(self.create_user, values=["c", "m"])
        self.role_entry.current(0)
        self.role_entry.grid(column=col+1, row=row+3, sticky=W, padx=5, pady=10)  
            
        self.create_user_btn = Button(self.create_user, command= create_user ,text= "Save", bg = "#20bebe")
        self.create_user_btn.grid(column=col+1, row=row+4, sticky=W, padx=5, pady=10)



        # View coodinators

        self.username_label = Label(self.view_coodinators, text="Username: ")
        self.username_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
   
           
        self.user_name_label = Label(self.view_coodinators, text="Name: ")
        self.user_name_label.grid(column=col+1, row=row+1, sticky=E, padx=5, pady=10)


        self.phone_label = Label(self.view_coodinators, text="Phone: ")
        self.phone_label.grid(column=col+2, row=row+1, sticky=E, padx=5, pady=10)


        def update_user(user):
            update_user = UpdateUser(user)
            update_user.mainloop()

        def delete_user(user):
            self.system.users.remove(user)
            self.destroy()
            self.__init__(self.system)

        def view_coodinators(event):
            coo = self.system.coodinators_objects
            # print(coo)
            # return
            for i, user in enumerate(coo):
                if user.role == 'c':
                # if user.role:
                            
                    username_view_label = Label(self.view_coodinators, text=user.username)
                    username_view_label.grid(column=col, row=row+2+i, sticky=W, padx=5, pady=10)  

                    user_name_view_entry = Label(self.view_coodinators, text=user.name)
                    user_name_view_entry.grid(column=col+1, row=row+2+i, sticky=W, padx=5, pady=10) 
                    
                    phone_entry = Label(self.view_coodinators, text=user.phone)
                    phone_entry.grid(column=col+2, row=row+2+i, sticky=W, padx=5, pady=10) 


                    coo_update = Button(self.view_coodinators,  text="Update", command=lambda: update_user(user), bg="yellow")
                    coo_update.grid(column=col+3, row=row+2+i, sticky=W, padx=5, pady=10) 

                    coo_del = Button(self.view_coodinators,  text="Delete", command=lambda: delete_user(user), bg="red")
                    coo_del.grid(column=col+4, row=row+2+i, sticky=W, padx=5, pady=10) 

        self.menu.bind('<<NotebookTabChanged>>', view_coodinators,  add='+')



        self.inv_username_label = Label(self.view_invoices, text="User Name: ")
        self.inv_username_label.grid(column=col, row=row+1, sticky=E, padx=5, pady=10)
        
        self.date_label = Label(self.view_invoices, text="Date: ")
        self.date_label.grid(column=col+1, row=row+1, sticky=E, padx=5, pady=10)

        self.trip_name_label = Label(self.view_invoices, text="Trip Name: ")
        self.trip_name_label.grid(column=col+2, row=row+1, sticky=E, padx=5, pady=10)
  

        self.amount_label = Label(self.view_invoices, text="Amount: ")
        self.amount_label.grid(column=col+3, row=row+1, sticky=E, padx=5, pady=10)


        self.traveller_label = Label(self.view_invoices, text="Traveller: ")
        self.traveller_label.grid(column=col+4, row=row+1, sticky=E, padx=5, pady=10)


        def update_invoice(invoice):
            update_invoice =  UpdateInvoice(invoice)
            update_invoice.mainloop()

        def delete_invoice(invoic):
            self.system.invoices.remove(invoic)
            self.destroy()
            self.__init__(self.system)

        def print_invoice(invoic):
            print()
            print(' Generating Invoice.....:')
            print(' Invoice Details:')
            print(' Invoice Number:', invoic.number)
            print(' Invoice Trip:', invoic.trip)
            print(' Invoice Amount:',invoic.amount)
            print(' Invoice Username:', invoic.username)
            print(' Invoice Traveller:', invoic.traveller_name)
            print(" Invoice Date:", invoic.date)
            print()
        
        def print_repceipt(invoic):     
            print()       
            print(' Generating Receipt.....:')
            print(' Receipt Details:')
            print(' Trip:', invoic.trip)
            print(' Amount:', invoic.amount)
            print(' Traveller:', invoic.traveller_name)
            print(" Date: ", invoic.date)
            print()

        def view_invoices(event):

            for i, invoice in enumerate(self.system.invoices):
                # print(invoice)
            
                inv_username_var= StringVar(self.view_invoices, value= invoice.username )
                inv_username_entry = Label(self.view_invoices, textvariable = inv_username_var, bg="white")
                inv_username_entry.grid(column=col, row=row+2+i, sticky=W, padx=5, pady=10)

                date_var= StringVar(self.view_invoices, value= invoice.date)
                date_entry = Label(self.view_invoices, textvariable = date_var , bg="white")
                date_entry.grid(column=col+1, row=row+2+i, sticky=W, padx=5, pady=10)  

                trip_name_var= StringVar(self.view_invoices, value= invoice.trip)
                trip_name_entry = Label(self.view_invoices, textvariable = trip_name_var , bg="white")
                trip_name_entry.grid(column=col+2, row=row+2+i, sticky=W, padx=5, pady=10)

                amount_var= StringVar(self.view_invoices, value= invoice.amount)
                amount_entry = Label(self.view_invoices, textvariable = amount_var)
                amount_entry.grid(column=col+3, row=row+2+i, sticky=W, padx=5, pady=10) 

                traveller_var= StringVar(self.view_invoices, value= invoice.traveller_name)
                traveller_entry = Label(self.view_invoices, textvariable = traveller_var)
                traveller_entry.grid(column=col+4, row=row+2+i, sticky=W, padx=5, pady=10) 

                

                inv_update = Button(self.view_invoices,  text="Update", command=lambda: update_invoice(invoice), bg="yellow")
                inv_update.grid(column=col+5, row=row+2+i, sticky=W, padx=5, pady=10) 

                inv_del = Button(self.view_invoices,  text="Delete", command=lambda: delete_invoice(invoice), bg="red")
                inv_del.grid(column=col+6, row=row+2+i, sticky=W, padx=5, pady=10) 

                inv_del = Button(self.view_invoices,  text="Print Invoice", command=lambda: print_invoice(invoice), bg="cyan")
                inv_del.grid(column=col+7, row=row+2+i, sticky=W, padx=5, pady=10) 

                inv_del = Button(self.view_invoices,  text="Print Receipt", command=lambda: print_repceipt(invoice), bg="blue", fg='white')
                inv_del.grid(column=col+8, row=row+2+i, sticky=W, padx=5, pady=10) 



        self.menu.bind('<<NotebookTabChanged>>', view_invoices,  add='+')


        def total_trips_invoices(event):
            self.view_total_invoices.grid_forget()
           
            total_trips_payments = Label(self.view_total_invoices, text="Total Trips Invoices and Payment",bg='cyan', font=("Arial", 16))
            total_trips_payments.grid(column=col, row=row, sticky=E, padx=(300, 5), pady=190) 

            total_trips_val= StringVar(self.view_total_invoices, value= system.total_invoices)
            total_trips_entry = Label(self.view_total_invoices, textvariable = total_trips_val, bg='cyan', font=("Arial", 16))
            total_trips_entry.grid(column=col+1, row=row, sticky=W, padx=(5, 300), pady=190) 
           


        self.menu.bind('<<NotebookTabChanged>>', total_trips_invoices,  add='+')