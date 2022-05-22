

from enums import IDType, TripDuration, TransportMode
import csv
import os

class Trip:
    trip_count = 0 
    def __init__(self, name, start_date,  duration,):
        Trip.trip_count += 1
        self.id = Trip.trip_count
        self.name = name
        self.start_date = start_date
        self.travellers = []
        self.trip_legs = []
        self.support_staff = []

            
        for dur in TripDuration:
            if dur.name == duration:
                duration = dur.value
                self.duration = duration
                break
            
            self.duration = None
            print(f" Invalid duration: {duration}")
        
        self.duration = duration

    def writeTripData(self):     
        header = ['id', 'name', 'start_date','travellers', 'trip_legs', 'support_staff']

        if os.path.isfile('data/trips.csv'):
            with open('data/camps.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([self.id, self.name, self.start_date, self.travellers, self.trip_legs, self.support_staff])

        else:
            with open('data/trips.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow([self.id, self.name, self.start_date, self.travellers, self.trip_legs, self.support_staff])


    def __repr__(self) -> str:
        return f"(Name {self.name}, Start Date {self.start_date})"
    
    def __str__(self) -> str:
        return f"The trip name is {self.name}, start date at: {self.start_date}"
    
    def create_trip_leg(self, start, destination, points_of_interests=[], transport_provider=None, transport_mode=None):
        new_trip_leg = TripLeg(start, destination, points_of_interests, transport_provider, transport_mode)
        self.trip_legs.append(new_trip_leg)

    def create_traveller(self, name, address=None,  birth_date=None, emr_contact = None ):
        new_traveller = Traveller(name, address,  birth_date, emr_contact)
        self.travellers.append(new_traveller)

    def view_traverllers(self):
        if self.travellers:
            for traveller in self.travellers:
                print(traveller.name)
        else:
            print("None")




class TripLeg:
    trip_leg_count = 0

    def __init__(self, starting_location, destination,points_of_interests= [],  transport_provider=None, transport_mode=None):
        TripLeg.trip_leg_count +=1
        self.trip_leg_id = TripLeg.trip_leg_count
        self.starting_location = starting_location
        self.destination = destination
        self.points_of_interests = points_of_interests
        self.transport_provider = transport_provider

        for vehicl in TransportMode:
            if vehicl.name == transport_mode:
                transport_mode = vehicl.value
                self.transport_mode = transport_mode
                break
        
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
        new_id = ID(type, number)
        self.gov_ids.append(new_id)
    
    def view_id(self):
        for id in self.gov_ids:
            print(id)
               
class ID:
    def __init__(self, type, number):
        self.number = number
        for id in IDType:
            if id.name == type:
                type = id.value
                self.id_type = type
                break
        
            self.id_type = None
            # print(f" Invalid ID type: {self.id_type}")
        
    def __repr__(self) -> str:
        return f"(ID Type {self.id_type}, ID Number {self.number})"
    
    def __str__(self) -> str:
        return f"(ID Type is {self.id_type}, ID Number is {self.number})"




passport = ID("national_id", 123456)
# print(passport.id_type)


trip_leg_1 = TripLeg("Solent", "park")

trip_leg_1.add_point_of_interest(['library'])

trip_leg_1.view_point_of_interests()

