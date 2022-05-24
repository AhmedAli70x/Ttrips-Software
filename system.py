from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



from tkTrips import Trips
from tkMain import MainMenu

class System:
    

    def __init__(self) -> None:
        self.trips = []

        menu_gui = MainMenu(self)
        menu_gui.mainloop()

        # gui = Trips(self)
        
        # gui.mainloop()



trips_system = System()

# print(trips_system.trips)