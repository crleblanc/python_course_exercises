#!/usr/bin/env python

# Example unit test using the unittest module, showing a Python class,
# methods, exceptions, assertions.
#
# Exercise: create a new class that inherits from Car(), call it ElectricCar.
# Unlike the normal car that has a 5 speed transmission our ElectricCar has
# reverse neutral (for this exercise) and one forward gear.  Write a new
# method for the ElectricCar class that will only accept -1 (reverse), 0 
# (neutral) or 1 (forwards).  Check with a unit test.

from __future__ import print_function
import unittest

class Car(object):
    def __init__(self):
        # indices for gears, 0 based.
        self.reverse_gear = -1
        self.neutral_gear = 0
        self.top_gear = 4
        self.gear = 0

    def shift(self, gear=0):
        """shift the transmission into the specified gear"""

        # error checking, the gear must be a valid number:
        if gear < self.reverse_gear or gear > self.top_gear:
            raise ValueError('gear must be between 0 and %s' % self.top_gear)

        self.gear = gear

class ElectricCar(Car):

    def __init__(self):
        super(ElectricCar, self).__init__()
        self.top_gear = 1

# Unit tests:
class TestClass(unittest.TestCase):

    def testCar(self):
        my_car = Car()
        # check the default gear, neutral
        self.assertEqual(my_car.gear, 0)

        # check shifting into reverse gear
        my_car.shift(-1)
        self.assertEqual(my_car.gear, -1)

        # check shifting into first gear
        my_car.shift(1)
        self.assertEqual(my_car.gear, 1)

        # check shifting into a gear we don't have
        self.assertRaises(ValueError, my_car.shift, -2)
        self.assertRaises(ValueError, my_car.shift, 5)

    def testElectricCar(self):
        """Test our new ElectricCar class"""
        pass

if __name__ == '__main__':
    unittest.main()
