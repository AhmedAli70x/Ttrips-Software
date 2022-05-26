from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



from tkTrips import Trips
from tkMain import MainMenu
from tkCreateTraveller import CreateTraveller
from trips import Traveller, Trip

class System: 
 
    def __init__(self) -> None:
        self.trips = []
        self.users = ['user1', 'user2', 'user3']

    def search_trip(self, id):
        if self.trips:
            for num in range(len(self.trips)):
                if self.trips[num].id == id+1:
                    return num
        messagebox.showinfo(title="TRIP ERROR", message="Trip Not Found",)
        return False


trip1 = Trip("Trip1",'10/06/2021')
trip1.create_traveller("traveller1", "address1",'22/10/99','4447140')
trip1.travellers[0].add_id('passport','123')
print(trip1.travellers[0].name)
system = System()
system.trips.append(trip1)

main_menu = MainMenu(system)
main_menu.mainloop()
