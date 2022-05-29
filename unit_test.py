import unittest





from trips import *

class TestTrips(unittest.TestCase):

    def test_trip(self):

        trip1 = Trip("Trip1", "22/05/1994", "1111", duration="one_day")

        self.assertEqual(trip1.name, "Trip1")
        self.assertEqual(trip1.start_date, "22/05/1994")
        self.assertEqual(trip1.contact_numer, "1111")
        self.assertEqual(trip1.duration, "one_day")
        self.assertEqual(trip1.support_staff_num, 0)

        trip1.travellers = [i for i in range(10)]
        self.assertEqual(trip1.support_staff_num, 1)

        trip1.travellers = [i for i in range(22)]
        self.assertEqual(trip1.support_staff_num, 2)

        #duation is assigned to None for any value outside the duration enum
        trip2 = Trip("Trip2", "22/06/1994", "2222", duration="one day")
        self.assertIsNone(trip2.duration, "Duration is None")

        






if __name__ == '__main__':
    unittest.main()



