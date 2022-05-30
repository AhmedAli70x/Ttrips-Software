from enum import Enum

class TripDuration(Enum):
   one_day = 0
   weekend = 1
   fortnight = 2

class TransportMode(Enum):
   plan = 0
   ferry = 1
   coach = 2
   taxi = 3

class IDType(Enum):
   passport = 1
   driving_license = 2
   national_id =  3

class UserRole(Enum):
   coodinator = 1
   manager = 2
   admin =  3





