#!/usr/bin/env python3

import unittest
from house_class import House

class House_Class_Test(unittest.TestCase):

    def test_house(self):
        house = House('123, lollipop rd', 'family', 4, 3)
        house.move_in()
        self.assertEqual(house.occupied, True)
        self.assertEqual(house.type, 'family')
        self.assertEqual(house.bedrooms, 4)
        self.assertEqual(house.bathrooms, 3)
        self.assertEqual(house.address, '123, lollipop rd')

unittest.main()