import unittest
from unittest import mock
import datetime
import time
from statistics import StaticsHandler as sts


class Test_Satatistics(unittest.TestCase):
    
    def setUp(self):
        y = 2022
        month = 1
        day = 16
        hour = 2
        minute = 13
        self.rand_time = str(datetime.datetime(
            y, month, day, hour, minute, 0).timestamp()).split('.')[0]
        self.stats = sts()
        

    def tearDown(self):
        pass

    def test_get_hour(self):
        self.assertEqual(self.stats.get_hour(self.rand_time), self.hour)
        
    def test_get_minute(self):
        self.assertEqual(self.stats.get_minute(self.rand_time), self.minute)
    
    def test_get_date(self):
        self.assertEqual(self.stats.get_date(self.midnight), f"{self.y}-{self.month}-{self.day}")

    def test_check_time(self):
        self.assertEqual(self.stats.check_time(self.rand_time, "hour"), True)
        self.assertEqual(self.stats.check_time(self.rand_time, "minute"), True)


if __name__ == "__main__":
   
    unittest.main()
