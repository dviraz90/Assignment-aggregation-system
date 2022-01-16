import unittest
from unittest.mock import patch
import datetime
import time
import os
import sys
import json
sys.path.insert(0, os.path.abspath(".."))
from src.statistics import StaticsHandler as sts




class Test_Satatistics(unittest.TestCase):
   
    def setUp(self):
        self.date1 = str(datetime.datetime(2022, 1, 16, 0, 1, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(2022, 1, 15, 23, 58, 0).timestamp()).split('.')[0]
        self.date3 = str(datetime.datetime(2022, 1, 16, 0, 0, 0).timestamp()).split('.')[0]
        self.date4 = str(datetime.datetime(2022, 1, 15, 23, 59, 0).timestamp()).split('.')[0]
        self.stats = sts()
        
    @classmethod
    def tearDown(self):
        #self.stat = sts()
        #self.stat.reset_db()
        pass
        
    

    # Test POST to DB
    
    def test_write_stats(self):
        data1 = {'timestamp': self.date3, 'A': 3, 'B': 45}
        data2 = {'timestamp': self.date2, 'H': 3, 'k': 4, 'C': 3, 'G': 6}
        data3 = {'timestamp': self.date4, 'A': 3, 'B': 45, 'O':67, 'D':95}
        data4 = {'timestamp': self.date1, 'D': 87, 'V': 14, 'I': 56, 'R': 2}
        self.assertEqual(self.stats.write_stats(data1), True)
        self.assertEqual(self.stats.write_stats(data2), True)
        self.assertEqual(self.stats.write_stats(data3), True)
        self.assertEqual(self.stats.write_stats(data4), True)


    # Test hour
    def test_get_hour(self):
        self.assertEqual(self.stats.get_hour(self.date1),0)
        self.assertEqual(self.stats.get_hour(self.date2), 23)
        self.assertEqual(self.stats.get_hour(self.date3), 0)
        self.assertEqual(self.stats.get_hour(self.date4), 23)


    #Test minute 
    def test_get_minute(self):
        self.assertEqual(self.stats.get_minute(self.date1), 1)
        self.assertEqual(self.stats.get_minute(self.date2), 58)
        self.assertEqual(self.stats.get_minute(self.date3), 0)
        self.assertEqual(self.stats.get_minute(self.date4), 59)


    #Test date
    def test_get_date(self):
        self.assertEqual(self.stats.get_date(self.date1),"2022-01-16")
        self.assertEqual(self.stats.get_date(self.date2), "2022-01-15")
        self.assertEqual(self.stats.get_date(self.date3), "2022-01-16")
        self.assertEqual(self.stats.get_date(self.date4), "2022-01-15")

    def test_domains_list(self):
        self.assertEqual(self.stats.domains_list(), 
                         [{"timestamp": "1642284000", "A": 3, "B": 45}, {"timestamp": "1642283880", "H": 3, "k": 4, "C": 3, "G": 6}, {"timestamp": "1642283940", "A": 3, "B": 45, "O": 67, "D": 95},  {"timestamp": "1642284060", "D": 87, "V": 14, "I": 56, "R": 2}])

    
   
    def test_top_ten_last_hour_domains(self):
        self.assertEqual(self.stats.top_ten_last_hour_domains(self.date3), [{'Domain': 'D', 'NumberOfRequests': 95}, {'Domain': 'O', 'NumberOfRequests': 67}, {'Domain': 'B', 'NumberOfRequests': 45}, {
                         'Domain': 'G', 'NumberOfRequests': 6}, {'Domain': 'k', 'NumberOfRequests': 4}, {'Domain': 'H', 'NumberOfRequests': 3}, {'Domain': 'C', 'NumberOfRequests': 3}, {'Domain': 'A', 'NumberOfRequests': 3}])
        
   
    def test_top_ten_last_minute_domains(self):
        self.assertEqual(self.stats.top_ten_last_minute_domains(self.date4), [{'Domain': 'G', 'NumberOfRequests': 6}, {
                         'Domain': 'k', 'NumberOfRequests': 4}, {'Domain': 'H', 'NumberOfRequests': 3}, {'Domain': 'C', 'NumberOfRequests': 3}])

    #def test_reset_db(self):
        #self.assertEqual(self.stats.reset_db(), True)



if __name__ == "__main__":
    unittest.main()
