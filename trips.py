

from pprint import pprint
from enums import IDType, TripDuration, TransportMode
import csv
import os

class Trip:
    trip_count =  0
    def __init__(self, name, start_date, contact_numer = 999999,  duration= "one_day"):
        Trip.trip_count += 1
        self.id = Trip.trip_count
        self.name = name
        self.start_date = start_date
        self.contact_numer = contact_numer
        self.travellers = []
        self.trip_legs = []
        self.support_staff = []
        
    

        for dur in TripDuration:
            if dur.name == duration:
                self.duration = duration
                break
            
            self.duration = None
        print(f" Duration is: {self.duration}")
 
        
    @property
    def support_staff_num(self):
        return round(len(self.travellers)/10)

    def __repr__(self) -> str:
        return f"(Name {self.name}, Start Date {self.start_date})"
    
    def __str__(self) -> str:
        return f"The trip name is {self.name}, start date at: {self.start_date}"
    
    def create_trip_leg(self, start, destination, point_of_interest, transport_provider=None, transport_mode=None):
        try:
            new_trip_leg = TripLeg(start, destination, point_of_interest, transport_provider, transport_mode)
            self.trip_legs.append(new_trip_leg)
            return True
        except:
            return False

    def create_traveller(self, name, address=None,  birth_date=None, emr_contact = None ):
        try:
            new_traveller = Traveller(name, address,  birth_date, emr_contact)
            self.travellers.append(new_traveller)
            return True
        except:
            return False

    def view_traverllers(self):
        if self.travellers:
            for traveller in self.travellers:
                print(traveller.name)
            return self.travellers
        else: 
            return False

    def view_travellers(self):
        if self.travellers:
            for traveller in self.travellers:
                print(traveller[0])
            return self.travellers
        else:
            print("No Travellers Found")
            return False

    def del_traveller(self, id):
        if self.travellers:
            for traveller in self.travellers:
                if traveller[0] == id:
                    self.travellers.remove(traveller)
                    print(f"Traveller rmoved")
                    return True      
            print("Not Found")
            return False
        else:
            print("No Travellers")
            return False
    
    def add_support_staff(self, support_staff):
        if  len(self.support_staff) < self.support_staff_num:
            self.support_staff.append(support_staff)
            return True
        else:
            print("Cannot add support staff")
            return False


class TripLeg:
    trip_leg_count = 0

    def __init__(self, starting_location, destination, point_of_interest,  transport_provider=None, transport_mode=None):
        TripLeg.trip_leg_count +=1
        self.trip_leg_id = TripLeg.trip_leg_count
        self.starting_location = starting_location
        self.destination = destination
        self.point_of_interest = point_of_interest
        self.transport_provider = transport_provider

        for vehicl in TransportMode:
            if vehicl.name == transport_mode:
                transport_mode = vehicl.name
                self.transport_mode = transport_mode
                break
        
            else:
                self.transport_mode = None
            # print(f" Invalid transport mode: {transport_mode}")
        
        
    def __repr__(self) -> str:
        return f"(Strating Location {self.starting_location}, Destination {self.destination})"
    
    def __str__(self) -> str:
        return f"Strating Location: {self.starting_location}, Destination: {self.destination}"
    
    def add_point_of_interest(self, points_list):
        for point in points_list:
            self.points_of_interests.append(point)
    
    def view_point_of_interests(self):
        if self.points_of_interests:
            for point in self.points_of_interests:
                print(point)
        else:
            print("None")
    


class Traveller:
    travellers_count = 0
    def __init__(self, name, address=None,  birth_date=None, emr_contact = None):
        Traveller.travellers_count +=1
        self.taveller_id = Traveller.travellers_count
        self.name = name
        self.address = address
        self.birth_date = birth_date
        self.emr_contact = emr_contact
        self.gov_ids = []
        
    def __repr__(self) -> str:
        return f"(Traveller name {self.name})"
    
    def __str__(self) -> str:
        return f"Traveller name is {self.name}"

    def add_id(self, type, number):
        new_id = Passport(type, number)
        self.gov_ids.append(new_id)
    
    def view_id(self):
        for id in self.gov_ids:
            print(id)
               
class Passport:
    def __init__(self, type, number, fullname=None, expirary_date=None, country=None):
        self.full_name = fullname
        self.expirary_date = expirary_date
        self.country = country
        self.number = number
        for id in IDType:
            if id.name == type:
                type = id.name
                self.id_type = type
                break
        
            self.id_type = None
            # print(f" Invalid ID type: {self.id_type}")
        
    def __repr__(self) -> str:
        return f"(ID Type {self.id_type}, ID Number {self.number})"
    
    def __str__(self) -> str:
        return f"(ID Type is {self.id_type}, ID Number is {self.number})"


#testing

# passport = ID("national_id", 123456)
# print(passport.id_type)


# trip_leg_1 = TripLeg("Solent", "park")

# trip_leg_1.add_point_of_interest(['library'])

# trip_leg_1.view_point_of_interests()

