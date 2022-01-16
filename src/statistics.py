import datetime
import json
from collections import Counter, defaultdict
import os

class StaticsHandler:
    data = defaultdict(lambda: {})

    get_hour = lambda self,epoch_time: int(str(datetime.datetime.fromtimestamp(float(epoch_time)))[11:].split(":")[0])
    '''Returns the current hour component according to the current epoch'''

    get_minute = lambda self,epoch_time: int(str(datetime.datetime.fromtimestamp(float(epoch_time)))[11:].split(":")[1]) 
    '''Returns the current minute component according to the current epoch'''

    get_date = lambda self, epoch_time: str(datetime.datetime.fromtimestamp(float(epoch_time)))[:10]
    '''Returns the current date component according to the current epoch'''
    

    def check_last_hour(self,epoch_time):
        domains = self.domains_list()
        last_hour_domains = []
        last_hour_epoch = int(epoch_time) - 3600 
        last_hour = self.get_hour(str(last_hour_epoch))
        day_last_hour = self.get_date(str(last_hour_epoch)[8:])
        for domain in domains:
            timestamp = domain["timestamp"]
            domain_day = self.get_date(str(timestamp)[8:])
            if self.get_hour(timestamp) == last_hour and day_last_hour == domain_day:
                last_hour_domains.append(domain)
        return last_hour_domains




    def check_last_minute(self, epoch_time):
        domains = self.domains_list()
        last_minute_domains = []
        last_minute_epoch = int(epoch_time) - 60
        last_minute = self.get_minute(str(last_minute_epoch))
        hour_last_minute = self.get_hour(str(last_minute_epoch))
        day_last_minute = self.get_date(str(last_minute_epoch)[8:])
        for domain in domains:
            timestamp = domain["timestamp"]
            domain_day = self.get_date(str(timestamp)[8:])
            domain_minute = self.get_minute(timestamp)
            domain_hour = self.get_hour(timestamp)
            if domain_minute == last_minute and domain_day == day_last_minute and domain_hour == hour_last_minute:
                last_minute_domains.append(domain)
        return last_minute_domains



    def get_last_round_hour_domains(self, epoch_time):
        ''' Calculates the last round hour according to the current epoch and
             returns list of domains according to that.
        '''

        domains_last_hour = []
        for domain in self.check_last_hour(epoch_time):
            # Create list of domains in the last round hour in a dictionary {"domain": numberOfRequests}
            for key, value in domain.items():
                # We want only the domains keys
                if key != "timestamp":
                    domains_last_hour.append({key: value})
        return domains_last_hour



    def get_last_round_minute_domains(self, epoch_time):
        ''' Calculates the last round minute according to the current epoch and
             returns list of domains according to that.
        '''
        domains_last_minute = []
        for domain in self.check_last_minute(epoch_time):
            # Create list of domains in the last round minute in a dictionary {"domain": numberOfRequests} 
            for key, value in domain.items():
                # We want only the domains keys
                if key != "timestamp":
                    domains_last_minute.append({key:value})
        return domains_last_minute



    def domains_list(self):
        '''Returns a list of all domains from db'''
        req_list = []
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "db.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        # Read from db.json
        with open(abs_file_path, 'r') as f:
            res = f.read()
            final = json.loads(res)
            for key in final.keys():
                req_list.append(final[key])
        return req_list


    def top_ten_last_minute_domains(self, epoch_time):
        ''' Returns the top 10 most common domains in the last minute
            according to their epoch, in a Dictionary stacture.'''
        top = 10
        #Getting all last round minute domains
        last_minute_domains = self.get_last_round_minute_domains(epoch_time)
        top_domains = defaultdict(lambda:0)
        for dom in last_minute_domains:
            for key, value in dom.items():
                top_domains[key] += value
        #If there are less than 10 domains , return all the domains in the dictionary
        if len(top_domains) < 10:
            top = len(top_domains)
       
        return [{"Domain": elem[0], "NumberOfRequests":elem[1]} for elem in Counter(top_domains).most_common(top)]


    def top_ten_last_hour_domains(self, epoch_time):
        ''' Returns the top 10 most common domains in the last hour
            according to their epoch, in a Dictionary stacture.'''
        top = 10
        #Getting all last round hour domains
        last_hour_domains = self.get_last_round_hour_domains(epoch_time)
        top_domains = defaultdict(lambda: 0)
        for dom in last_hour_domains:
            for key, value in dom.items():
                top_domains[key] += value
        #If there are less than 10 domains , return all the domains in the dictionary
        if len(top_domains) < 10:
            top = len(top_domains)
        return [{"Domain": elem[0], "NumberOfRequests":elem[1]} for elem in Counter(top_domains).most_common(top)]


    key = 0
    def write_stats(self, req_data):
        ''' Writes stats to db  '''
        for self.key, value in StaticsHandler.data.items():
            pass
        index = int(self.key)+1
        StaticsHandler.data[index] = req_data
        script_dir = os.path.dirname(__file__)
        rel_path = "db.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'w+') as file_data:
            json.dump(StaticsHandler.data, file_data)
        return True

    
    def reset_db(self):
        '''Delete DB content '''
        script_dir = os.path.dirname(__file__)
        rel_path = "db.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.key = 0
        with open(abs_file_path, 'w+') as file_data:
            StaticsHandler.data.clear()
            json.dump(StaticsHandler.data, file_data)
        return True
        
