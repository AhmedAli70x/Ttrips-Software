from enum import Enum

class TripDuration(Enum):
   one_day = 1
   weekend = 2
   fortnight = 3

class TransportMode(Enum):
   plan = 1
   ferry = 2
   coach = 3
   taxt = 4


class IDType(Enum):
   passport = 1
   driving_license = 2
   national_id =  3

class UserRole(Enum):
   coodinator = 1
   manager = 2
   admin =  3






