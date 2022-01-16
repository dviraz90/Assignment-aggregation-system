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
    

    def check_last_time(self, epoch_time, time_comp):
        ''' Check the last hour/minute for eche domain in the domains list.
            and add them to the matched list.
            params: 
                epoch_time - float number that represents date and time.
                time_comp - str "minute or "hour", represents the time component.

            returns: dictionary of the 2 lists
        '''
        # Set times variables. 
        current_hour, current_minute = self.get_hour(
            epoch_time), self.get_minute(epoch_time)
        current_day = int(self.get_date(epoch_time)[8:])
        domains = self.domains_list()
        last_minute = current_minute - 1
        last_hour = current_hour - 1
        last_day = current_day - 1
        minute_count = []
        hour_count = []

        for domain in domains:
            timestamp_minute = self.get_minute(domain["timestamp"]),
            timestamp_hour = self.get_hour(domain["timestamp"])
            timestamp_day = int(self.get_date(domain["timestamp"])[8:])
            # If the given time component is aminute
            if time_comp == "minute":
                # Check if domain's minute equals to current minute
                # Check if domain's minute equals to last_minute % 60 - for midnight case
                # Check if domain's day equals to last day - for midnight case
                if (timestamp_minute == last_minute and current_day == timestamp_day or
                        timestamp_minute == last_minute % 60 and last_day == timestamp_day):
                    minute_count.append(domain)

            # If the given time component is aminute
            elif time_comp == "hour":
                # Same logic as above
                if (timestamp_hour == last_hour and current_day == timestamp_day or
                        timestamp_hour == last_hour % 24 and last_day == timestamp_day):
                    hour_count.append(domain)
      
        return {"hour":hour_count,"minute": minute_count}


    def get_last_round_hour_domains(self, epoch_time):
        ''' Calculates the last round hour according to the current epoch and
             returns list of domains according to that.
        '''

        domains_last_hour = []
        last_hour = self.check_last_time(epoch_time, "hour")
        for domain in last_hour["hour"]:
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
        last_minute = self.check_last_time(epoch_time, "minute")
        for domain in last_minute["minute"]:
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
        
        for self.key, value in StaticsHandler.data.items():
            pass
        index = int(self.key)+1
        StaticsHandler.data[index] = req_data
        script_dir = os.path.dirname(__file__)
        rel_path = "db.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'w+') as file_data:
            json.dump(StaticsHandler.data, file_data)

    
    def reset_db(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "db.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        os.remove(abs_file_path)
        return True
        
