import unittest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
import time
import os
import sys
import json
sys.path.insert(0, os.path.abspath(".."))
from src.statistics import StaticsHandler as sts




class Test_Satatistics(unittest.TestCase):
    mock_time = Mock()
    mock_time.return_value = time.mktime(datetime.datetime(2022, 1, 16,0,0,0).timetuple())

    def setUp(self):
        self.date1 = str(datetime.datetime(2022, 1, 16, 14, 0, 0).timestamp()).split('.')[0]
        self.date2 = str(datetime.datetime(2022, 1, 16, 14, 56, 0).timestamp()).split('.')[0]
        self.date3 = str(datetime.datetime(2022, 1, 16, 0, 0, 0).timestamp()).split('.')[0]
        self.date4 = str(datetime.datetime(2022, 1, 15, 23, 59, 0).timestamp()).split('.')[0]
        self.stats = sts()
        

    def tearDown(self):
        self.stats.reset_db()
        
    
    @patch("time.time", mock_time)
    def test_write_stats(self):
        data1 = {'timestamp': str(int(time.time())), 'A': 3, 'B': 45}
        data2 = {'timestamp': self.date1, 'A': 3, 'B': 4, 'C': 3, 'G': 6}
        data3 = {'timestamp': self.date3, 'A': 3, 'B': 45, 'D':67, 'G':95}
        data4 = {'timestamp': self.date4, 'A': 87, 'B': 14, 'C': 56, 'G': 2}
        self.assertEqual(self.stats.write_stats(data1), None)
        self.assertEqual(self.stats.write_stats(data2), None)
        self.assertEqual(self.stats.write_stats(data3), None)
        self.assertEqual(self.stats.write_stats(data4), None)


    def test_get_hour(self):
        self.assertEqual(self.stats.get_hour(self.date1),14)
        self.assertEqual(self.stats.get_hour(self.date2), 14)
        self.assertEqual(self.stats.get_hour(self.date3), 0)
        self.assertEqual(self.stats.get_hour(self.date4), 23)
        
    def test_get_minute(self):
        self.assertEqual(self.stats.get_minute(self.date1), 0)
        self.assertEqual(self.stats.get_minute(self.date2), 56)
        self.assertEqual(self.stats.get_minute(self.date3), 0)
        self.assertEqual(self.stats.get_minute(self.date4), 59)
    
    def test_get_date(self):
        self.assertEqual(self.stats.get_date(self.date1),"2022-01-16")
        self.assertEqual(self.stats.get_date(self.date2), "2022-01-16")
        self.assertEqual(self.stats.get_date(self.date3), "2022-01-16")
        self.assertEqual(self.stats.get_date(self.date4), "2022-01-15")

    
    def test_check_time(self):
        self.assertEqual(self.stats.check_last_time(self.date4, "hour"), {"hour": [], "minute": []})
        self.assertEqual(self.stats.check_last_time(self.date4, "minute"), { "hour": [],"minute": []})

    #@patch("time.time", mock_time)
   # def test_top_ten_last_hour_domains(self):
        #self.assertEqual(self.stats.top_ten_last_hour_domains(
            #time.time()), [{'Domain': 'B', 'NumberOfRequests': 3600}, {'Domain': 'A','NumberOfRequests': 120}])
        
   # @patch("time.time", mock_time)
   # def test_top_ten_last_minute_domains(self):
        #self.assertEqual(self.stats.top_ten_last_minute_domains(
            #time.time()),  [])
    def test_reset_db(self):
        self.assertEqual(self.stats.reset_db(), True)


if __name__ == "__main__":
    unittest.main()
