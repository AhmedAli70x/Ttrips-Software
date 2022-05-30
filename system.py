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

    def login(self, username, password ):
        for user in self.users:
            if user.username == username and user.password == password:
                self.cur_user = user
                if isinstance(user, Administrator):
                    System.login_user = "admin" 
                elif isinstance(user, Manager):
                    System.login_user = "manager"
                elif isinstance(user, Coodinator):
                    System.login_user = "coodinator"
                
            else:
                messagebox.showerror("Invalid Login", "Invalid Login, please try again")


    def search_trip(self, id):
        if self.trips:
            for num in range(len(self.trips)):
                if self.trips[num].id == id+1:
                    return num
        messagebox.showinfo(title="TRIP ERROR", message="Trip Not Found",)
        return False


    def refresh(self):
        self.destroy()
        self.__init__()

trip1 = Trip("Trip1",'10/06/2021')
trip1.create_traveller("traveller1", "address1",'22/10/99','4447140')
trip1.travellers[0].add_id('passport1','123', 'Jacob Jack2', "25/07/2024", "Chzech")

trip1.create_traveller("traveller2", "address1",'22/10/99','4447140')
trip1.travellers[0].add_id('passport2','123', 'Jacob Jack2', "25/07/2024", "Chzech")
system = System()
system.trips.append(trip1)
admin = Administrator('admin', "Luise Diase", '123')
system.users.append(admin)
# system.login('admin', "123")

login_gui = LoginGUI(system)
login_gui.mainloop()

# main_gui = MainMenu(system)
# main_gui.mainloop()


