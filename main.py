


trip_list = [['coordinator','co123', ]]
user_list = []
from enums import UserRole

print(UserRole.coodinator.name)


class Coodinator:
    def __init__(self, username, password, phone):

        self.username = username
        self.password = password
        self.phone = phone
        self.user_role = UserRole.coodinator.name    
    
    def create_trip(self)

class Manager(Coodinator):
    def __init__(self, username, password, phone):
        super.__init__(username, password, phone)
        self.user_role = UserRole.manager.name    



class Admin(Manager):
    def __init__(self, username, password, phone):
        super.__init__(username, password, phone)
        self.user_role = UserRole.admin.name    


    


class TripSystem:

    def __init__(self):

        self.trip_list = []
        self.user_list = []

    




