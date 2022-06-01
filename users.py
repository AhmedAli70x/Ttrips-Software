



class Coodinator:
    def __init__(self, username, name, phone, system=None ):
        self.username = username
        self.name = name
        self.phone =phone
        self.system = system
        self.role = 'c'
        self.trip = None

    def view_trips(self):
        pass

    def create_travller(self):
        pass
    def view_travellers(self):
        pass
    def update_traveller(self):
        pass

    def delete_traveller(self):
        pass

    def create_trip_leg(self):
        pass
    def view_trip_legs(self):
        pass
    def update_trip_leg(self):
        pass

    def take_payment(self):
        pass

class Manager(Coodinator):
    def __init__(self,  username, name, phone, system=None):
        super().__init__( username, name, phone, system)
        self.managed_trips = []
        self.role = 'm'

    
    def add_trip(self, trip):
        self.managed_trips.append(trip)

    def create_trip():
        pass

    def update_trip():
        pass
    
    def del_trip():
        pass

    def create_coodinator():
        pass

    def view_coodinators():
        pass
    def update_coodinator():
        pass

    def delete_coodinator():
        pass

    def total_trip_invoice():
        pass


class Administrator(Manager):
    def __init__(self,  username, name, phone, system=None):
        super().__init__( username, name, phone, system)
        self.role = 'a'

    
    def create_manager():
        pass

    def view_managers():
        pass
    def update_manager():
        pass

    def delete_manager():
        pass

    def total_trips_invoice():
        pass
    


# coodinator  = Coodinator("coodinator", "123")
# check1 = isinstance(coodinator, Coodinator)
# print(check1)


# mananger = Manager("manager", "123")

# check2 = isinstance(mananger, Coodinator)
# print(check2)


# admin = Administrator("admin", '123')

# check3 = isinstance(mananger, Administrator)
# print(check3)
