import json
import time
import requests
import random


class Requests:
    # Function for sending requests
    def send_requests(self, data):
        ''' This function sends POST requests to http://localhost:8000/api/events '''
        r = requests.post("http://localhost:8000/api/events", data=json.dumps(data))
        if r.status_code == 200:
            return 'Ok'
        return 'Bad Request'


    # Functions to get the statistic.
    def get_minutes_requests(self):
        '''This function prints statistics for top last minutes'''
        m = requests.get("http://localhost:8000/api/stats/minutes")
        if m.status_code == 200:
            return 'OK'
        return 'Bad Request'


    def get_hours_requests(self):
        '''This function prints statistics for top last hours'''
        h = requests.get("http://localhost:8000/api/stats/hours")
        if h.status_code == 200:
            return 'OK'
        return 'Bad Request'

   
    
