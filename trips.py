
from enums import IDType, TripDuration, TransportMode
from invoice  import Invoice
from datetime import datetime


class Trip:
    trip_count =  0
    def __init__(self, name, start_date, trip_coodinator= None, trip_manager= None,  duration= "one_day"):
        Trip.trip_count += 1
        self.id = Trip.trip_count
        self.name = name
        self.start_date = start_date
        self.trip_coodinator = trip_coodinator
        self.trip_manager = trip_manager
        self.travellers = []
        self.trip_legs = []
        self.support_staff = []
        self.payments = []
        

        for dur in TripDuration:
            if dur.name == duration:
                self.duration = duration
                break
            self.duration = None
        # print(f" Duration is: {self.duration}")
 
        
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
                print(traveller)
            return self.travellers
        else: 
            return False

    def view_trip_legs(self):
        if self.travellers:
            for trip_leg in self.trip_legs:
                print(trip_leg)
            return self.travellers
        else:
            print("No Trip Legs Found")
            return False

    def del_traveller(self, id):
        if self.travellers:
            try:
                self.travellers.pop(id)
                print(f"Traveller removed")
                return True 
            except:
                print(f"{id} out of index")  
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

    
    def take_payment(self, amount, trip=None, username=None, traveller_name=None, date=datetime.today().strftime('%Y-%m-%d') ):
        new_payment = Invoice(amount, trip, username, traveller_name, date)
        self.payments.append(new_payment)



    @property
    def total_invoice(self):
        total_payments = 0
        for invoice in self.payments:
            total_payments += invoice.amount

        # print(total_payments)
        return(total_payments)
    


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
                self.transport_mode = transport_mode
                break
        
            else:
                self.transport_mode = None
            # print(f" Invalid transport mode: {transport_mode}")
        
        
    def __repr__(self) -> str:
        return f"(Strating Location {self.starting_location}, Destination {self.destination})"
    
    def __str__(self) -> str:
        return f"Strating Location: {self.starting_location}, Destination: {self.destination}"
    

    

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

    def create_id(self, type, number, fullname, expiry_date, country):
        try:
            new_passport = Passport(type, number, fullname, expiry_date, country)
            self.gov_ids.append(new_passport)
            return True
        except:
            return False

    def view_id(self):
        for id in self.gov_ids:
            print(id)

               
class Passport:
    def __init__(self, type, number, fullname=None, expiry_date=None, country=None):
        self.full_name = fullname
        self.expiry_date = expiry_date
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




