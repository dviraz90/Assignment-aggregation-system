from http.server import HTTPServer
import unittest
from unittest.mock import patch, Mock
import datetime
import time
import os
import sys
sys.path.insert(0, os.path.abspath(".."))
from src.server import ServiceHandler



class Test_Requests(unittest.TestCase):
    mock_time = Mock()
    def setUp(self):
        pass
        
    def tearDown(self):
        self.handler = None

   
    # Test POST requests
    def test_do_POST(self):
        self.date1 = str(datetime.datetime(2022, 1, 15, 23, 59, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(2022, 1, 16, 0, 0, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(2022, 1, 16, 1, 45, 0).timestamp()).split('.')[0]
        
        
        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date1, 'A': 3, 'B': 45}), None)
        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date2, 'D': 65, 'F': 120}), None)
        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date3, 'K': 37, 'C': 2, 'D': 6, 'F': 8}), None)

    mock_time.return_value = time.mktime(datetime.datetime(2022, 1, 16, 0, 0, 0).timetuple())

   
    def test_do_GET(self):
        self.date1 = str(datetime.datetime(
            2022, 1, 15, 23, 59, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(
            2022, 1, 16, 0, 0, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(
            2022, 1, 16, 1, 45, 0).timestamp()).split('.')[0]


        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date1, 'A': 3, 'B': 45}), None)
        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date2, 'D': 65, 'F': 120}), None)
        self.assertEqual(self.handler.do_POST(
            {'timestamp': self.date3, 'K': 37, 'C': 2, 'D': 6, 'F': 8}), None)

        self.date = time.time()
        self.assertEqual(self.handler.do_GET(time.time()), None)
        


if __name__ == "__main__":
    unittest.main()
