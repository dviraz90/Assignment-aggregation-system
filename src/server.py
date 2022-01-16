from http.server import  BaseHTTPRequestHandler, HTTPServer
from collections import defaultdict
import json
import time
import os,sys
sys.path.insert(0, os.path.abspath("."))
from statistics import StaticsHandler


global data
data = defaultdict(lambda: {})

#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
    
    
    # sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        #reads the length of the Headers
        length = int(self.headers['Content-Length'])
        #reads the contents of the request
        content = self.rfile.read(length)
        headers = str(content).strip('b\'')
        self.end_headers()
        return headers

    # GET Method Defination
    def do_GET(self):
        stats = StaticsHandler()
        
        t = time.time()
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        if self.path == '/api/stats/minutes':
            minutes = stats.top_ten_last_minute_domains(t)
            self.wfile.write(json.dumps(minutes).encode())
        elif self.path == '/api/stats/hours':
            hours = stats.top_ten_last_hour_domains(t)
            self.wfile.write(json.dumps(hours).encode())
        else:
            pass
       
        
        
    #POST method defination
    def do_POST(self):
        headers = self._set_headers()
        stats = StaticsHandler()
        if self.path == "/api/events":
            data = json.loads(headers)
            #write the changes to the json file
            stats.write_stats(data)
        else:
            pass
    

#Server Initialization

server = HTTPServer(('', 5000), ServiceHandler)
server.serve_forever()
