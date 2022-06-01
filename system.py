from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



from tk_trips import Trips
from tk_main import MainMenu
from tk_create_traveller import CreateTraveller
from trips import Traveller, Trip
from tk_login import LoginGUI
from users import *


class System: 
    login_user = None

    def __init__(self) -> None:
        self.trips = []
        self.users = []
        self.cur_user = None
        self.trip_tot_invoices = []

    def login(self, username ):
        for user in self.users:
            if user.username == username :
                self.cur_user = user
                if isinstance(user, Administrator):
                    System.login_user = "admin" 
                elif isinstance(user, Manager):
                    System.login_user = "manager"
                elif isinstance(user, Coodinator):
                    System.login_user = "coodinator"
                break
                

        if not System.login_user:
            messagebox.showerror("Invalid Login", "Invalid Login, please try again")

    @property
    def system_coodinators(self):
        coodinators_list = []
        for user in self.users:
            if user.role == 'c':
                coodinators_list.append(user.name)
        return coodinators_list

    @property
    def system_managers(self):
        self.managers_list = []
        for user in self.users:
            if user.role == 'm':
                self.managers_list.append(user.name)
        return self.managers_list

    @property
    def coodinators_objects(self):
        self.coodinators_list = []
        for user in self.users:
            if user.role == 'c':
                self.coodinators_list.append(user)
        return self.coodinators_list

    @property
    def managers_objects(self):
        self.managers_list = []
        for user in self.users:
            if user.role == 'm':
                self.managers_list.append(user)
        return self.managers_list

    @property
    def invoices(self):
        all_invoices = []
        for trip in self.trips:
            all_invoices += trip.payments
        return all_invoices


    @property
    def total_invoices(self):
        self.total = 0
        for trip in self.trips:
            self.total += trip.total_invoice
        return self.total


    def search_trip(self, name):
        if self.trips:
            for trip in self.trips:
                if trip.name == name:
                    return trip
            return False
        # messagebox.showinfo(title="TRIP ERROR", message="Trip Not Found",)
        else:
            return False

    def search_user(self, name):
        if self.users:
            for user in self.users:
                if user.name == name:
                    return user
            return False
        # messagebox.showinfo(title="ERROR", message="User Not Found",)
        else:
            return False


    def refresh(self):
        self.destroy()
        self.__init__()

trip1 = Trip("Trip1",'10/06/2021')
trip1.create_traveller("traveller1", "address1",'22/10/99','4447140')
trip1.travellers[0].create_id('passport1','123', 'Jacob Jack2', "25/07/2024", "Chzech")

trip1.create_traveller("traveller2", "address1",'22/10/99','4447140')
trip1.travellers[0].create_id('passport2','123', 'Jacob Jack2', "25/07/2024", "Chzech")
system = System()
system.trips.append(trip1)
admin = Administrator('admin', "Luise Diase", '123')
coo1 = Coodinator('coo', "Manie Mark", '123')
trip1.trip_coodinator = coo1

cood2 = Coodinator('coo2', "Luka James", '999')

man1 = Manager('man1', "Jacob Adam", '123')
man2 = Manager('man2', "Sara Henry", '123')

admin = Administrator('admin', "Luise Diase", '123')
system.users.append(admin)
system.users.append(coo1)
system.users.append(cood2)
system.users.append(man1)
system.users.append(man2)
trip1.trip_coodinator = coo1
trip1.take_payment(10)
trip1.take_payment(20)
trip1.take_payment(10)
# print(trip1.coodinator)
# print(trip1.contact)
# print(system.system_managers)
# print(trip1.total_invoice)
trip2 = Trip("Trip2", "22/06/1994", "2222", duration="one day")
system.trips.append(trip2)
trip2.take_payment(20)

# print(system.total_invoices)
# print(system.invoices)


# system.login('admin', "123")

# main_gui = MainMenu(system)
# main_gui.mainloop()

if __name__ == "__main__":
        
    login_gui = LoginGUI(system)
    login_gui.mainloop()



