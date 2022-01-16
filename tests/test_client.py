import unittest
import datetime
import random as rnd
import src.client
from client import Requests as req


class Test_Requests(unittest.TestCase):

    def setUp(self):
        self.client = req()
        y = 2022
        month = 1
        day = 16
        hour = rnd.randint(0, 59)
        minute = rnd.randint(0, 59)
        self.data = str(datetime.datetime(
            y, month, day, hour, minute, 0).timestamp()).split('.')[0]

    def tearDown(self):
        pass

    def test_send_requests(self):
        self.assertEqual(self.client.send_requests(self.data), "Ok")
        self.assertEqual(self.client.send_requests(self.data), "Bad Request")
