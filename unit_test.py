import unittest

from system import System

from trips import *
from users import * 

class TestSystem(unittest.TestCase):

    def test_trip(self):
        coo1 = Coodinator('coo', "Manie Mark", '1111')

        trip1 = Trip("Trip1", "22/05/1994", "1111", duration="one_day")
        self.assertEqual(trip1.name, "Trip1")
        self.assertEqual(trip1.start_date, "22/05/1994")
        trip1.trip_coodinator = coo1
        self.assertEqual(trip1.trip_coodinator.phone, "1111")
        self.assertEqual(trip1.duration, "one_day")
        self.assertEqual(trip1.support_staff_num, 0)

        trip1.travellers = [i for i in range(10)]
        self.assertEqual(trip1.support_staff_num, 1)

        add_support_staff1 = trip1.add_support_staff("Hassan")
        self.assertTrue(add_support_staff1)

        trip1.travellers = [i for i in range(22)]
        self.assertEqual(trip1.support_staff_num, 2)

        #duation is assigned to None for any value outside the duration enum


        trip2 = Trip("Trip2", "22/06/1994", "2222", duration="one day")
        create_trip_leg = trip2.create_trip_leg("Start Location", "Maritime Museum", "National Park")
        self.assertTrue(create_trip_leg)


        create_traveller = trip2.create_traveller("Luca", "Fareham", "22/09/1999")
        create_traveller = trip2.create_traveller("Chris", "Morocco", "22/09/1999")
        create_traveller = trip2.create_traveller("Mona", "Chilie", "22/09/1999")
        self.assertTrue(create_traveller)
        # trip2.view_traverllers()

        del_trveller = trip2.del_traveller(0)
        self.assertTrue(del_trveller)
        # trip2.view_traverllers()

        self.assertEqual(trip2.support_staff_num, 0)
        add_support_staff = trip2.add_support_staff("Hassan")
        self.assertFalse(add_support_staff)

        trip2.take_payment(10)
        trip2.take_payment(20)
        trip2.take_payment(30)
        trip_toatl = trip2.total_invoice
        self.assertEqual(trip_toatl, 60)


    def TestTripLeg(self):
        trip_leg1 = TripLeg("POintA", "POintB", "Mid Point", "KG Transport", "ferry")
        self.assertTrue(trip_leg1.starting_location in "POintA")
        self.assertTrue(trip_leg1.destination in "POintB")
        self.assertTrue(trip_leg1.point_of_interest in  "Mid Point")
        self.assertTrue(trip_leg1.transport_provider in  "KG Te2eeansport")
        self.assertTrue(trip_leg1.transport_mode in  "ferry")
        print(trip_leg1.transport_mode)




    
    def TestTraveller(self):

        traveller1  = Traveller("Benn", "Home Adddess", "25/05/2002", "999999")

        self.assertTrue(traveller1.name in "Benn")
        self.assertTrue(traveller1.address in "Home Adddess")
        self.assertTrue(traveller1.birth_date in  "25/05/2002")
        self.assertTrue(traveller1.emr_contact in  "999999")

        add_pass = traveller1.add_id('Passport', '55555', 'Jack Lio', '25/07/2023', 'Germany')
        self.assertFalse(add_pass)


    def TestUsers(self):

        coodinator  = Coodinator("coodinator", "123")
        mananger = Manager("manager", "123")
        admin = Administrator("admin", '123')

        self.assertTrue(isinstance(coodinator, Coodinator))

        self.assertFalse(isinstance(coodinator, Manager))
        self.assertTrue(isinstance(mananger, Manager))

        self.assertFalse(isinstance(coodinator, Administrator))
        self.assertFalse(isinstance(mananger, Administrator))
        self.assertTrue(isinstance(admin, Administrator))

    def System(self):
        trip1 = Trip("Trip1",'10/06/2021')
        trip1.create_traveller("traveller1", "address1",'22/10/99','4447140')
        trip1.travellers[0].create_id('passport1','123', 'Jacob Jack2', "25/07/2024", "Chzech")

        trip1.create_traveller("traveller2", "address1",'22/10/99','4447140')
        trip1.travellers[0].create_id('passport2','123', 'Jacob Jack2', "25/07/2024", "Chzech")
        system = System()
        system.trips.append(trip1)
        admin = Administrator('admin', "Luise Diase", '123')
        coo1 = Coodinator('coo', "Manie Mark", '123')
        trip1.trip_coodinator = coo1

        cood2 = Coodinator('coo2', "Luka James", '999')

        man1 = Manager('man1', "Jacob Adam", '123')
        man2 = Manager('man2', "Sara Henry", '123')

        admin = Administrator('admin', "Luise Diase", '123')
        system.users.append(admin)
        system.users.append(coo1)
        system.users.append(cood2)
        system.users.append(man1)
        system.users.append(man2)
        trip1.trip_coodinator = coo1
        trip1.take_payment(10)
        trip1.take_payment(20)
        trip1.take_payment(10)
        self.assertEqual(trip1.total_invoice, 40)

        trip2 = Trip("Trip2", "22/06/1994", "2222", duration="one day")
        system.trips.append(trip2)
        trip2.take_payment(20)
        self.assertEqual(system.total_invoices, 60)
        self.assertTrue(system.invoices)









if __name__ == '__main__':
    unittest.main()



