import datetime
import json
import requests

PORT = 5000

class Requests:
    # Function for sending requests
    def send_requests(self, data):
        ''' This function sends POST requests to http://localhost:8000/api/events '''
        r = requests.post("http://localhost:5000/api/events", data=json.dumps(data))
        if r.status_code == 200:
            return 'Ok'
        return 'Bad Request'


    # Functions to get the statistic.
    def get_minutes_requests(self):
        '''This function prints statistics for top last minutes'''
        m = requests.get("http://localhost:5000/api/stats/minutes")
        if m.status_code == 200:
            return m.text
        return 'Bad Request'


    def get_hours_requests(self):
        '''This function prints statistics for top last hours'''
        h = requests.get("http://localhost:5000/api/stats/hours")
        if h.status_code == 200:
            return h.text
        return 'Bad Request'

req = Requests()  
for i in range(10):
    r = req.send_requests(({"timestamp": str(datetime.datetime(
    2022, 1, 15, 23, 59, 0).timestamp()).split('.')[0] ,"A":3,"B":90}))
    print(r)
#print(req.get_minutes_requests())
#print(req.get_hours_requests())
