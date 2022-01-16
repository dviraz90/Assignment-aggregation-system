from http.server import  BaseHTTPRequestHandler, HTTPServer
from collections import defaultdict
from statistics import StaticsHandler
import json
import time


#Defining a class to Handle the statistics



#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
    data = defaultdict(lambda: {})
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
        if self.path == "/api/events":
            key = 0
            #getting key and value of the data dictionary
            for key, value in self.data.items():
                pass
            index = int(key)+1
            self.data[index] = json.loads(headers)
            #write the changes to the json file
            with open("db.json", 'w+') as file_data:
                json.dump(self.data, file_data)
            #self.wfile.write(json.dumps(data[str(index)]).encode())
        else:
            pass
    

#Server Initialization
server = HTTPServer(('', 8000), ServiceHandler)
server.serve_forever()
