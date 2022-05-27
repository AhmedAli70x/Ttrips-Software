

from tkinter.messagebox import NO


class Coodinator:
    def __init__(self, username, password,system, phone=None ):
        self.username = username
        self.password = password
        self.phone =phone
        self.system = system

    def create_trip():
        pass

class Manager(Coodinator):
    def __init__(self, username, password, phone = None):
        super().__init__(username, password, phone)


class Administrator(Manager):
    def __init__(self, username, password, phone=None):
        super().__init__(username, password, phone)


    
    