import datetime
import json
from collections import Counter, defaultdict

class StaticsHandler:
 
    get_hour = lambda self,epoch_time: int(str(datetime.datetime.fromtimestamp(float(epoch_time)))[11:].split(":")[0])
    '''Returns the current hour component according to the current epoch'''

    get_minute = lambda self,epoch_time: int(str(datetime.datetime.fromtimestamp(float(epoch_time)))[11:].split(":")[1]) 
    '''Returns the current minute component according to the current epoch'''

    get_date = lambda self, epoch_time: str(datetime.datetime.fromtimestamp(float(epoch_time)))[:10]
    '''Returns the current date component according to the current epoch'''
    

    def check_time(self, epoch_time, time_comp):

        current_hour, current_minute = self.get_hour(
            epoch_time), self.get_minute(epoch_time)
        current_day = int(self.get_date(epoch_time)[8:])
        domains = self.domains_list()
        last_minute = current_minute - 1
        last_hour = current_hour - 1
        last_day = current_day - 1

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
                    return True

            # If the given time component is aminute
            elif time_comp == "hour":
                # Same logic as above
                if (timestamp_hour == last_hour and current_day == timestamp_day or
                        timestamp_hour == last_hour % 24 and last_day == timestamp_day):
                    return True
        return False


    def get_last_round_hour_domains(self, epoch_time):
        ''' Calculates the last round hour according to the current epoch and
             returns list of domains according to that.
        '''

        domains_last_hour = []
        for domain in self.domains_list():
            # Validate last hour
            if self.check_time(epoch_time, "hour"):
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
        for domain in self.domains_list():
            # Validate last minute
            if self.check_time(epoch_time, "minute"):
                # Create list of domains in the last round minute in a dictionary {"domain": numberOfRequests} 
                for key, value in domain.items():
                    # We want only the domains keys
                    if key != "timestamp":
                        domains_last_minute.append({key:value})
        return domains_last_minute


    def domains_list(self):
        req_list = []
        with open("db.json", 'r') as f:
            res = f.read()
            res = json.loads(res)
            for key in res.keys():
                req_list.append(res[key])
        return req_list


    def top_ten_last_minute_domains(self, epoch_time):
        top = 0
        last_minute_domains = self.get_last_round_minute_domains(epoch_time)
        top_domains = defaultdict(lambda:0)
        for dom in last_minute_domains:
            for key, value in dom.items():
                top_domains[key] += value
        if len(top_domains) >= 10:
            top = 10
        else:
            top = len(top_domains)
        return [{"Domain": elem[0], "NumberOfRequests":elem[1]} for elem in Counter(top_domains).most_common(top)]


    def top_ten_last_hour_domains(self, epoch_time):
        top = 0
        last_hour_domains = self.get_last_round_hour_domains(epoch_time)
        top_domains = defaultdict(lambda: 0)
        for dom in last_hour_domains:
            for key, value in dom.items():
                top_domains[key] += value
        if len(top_domains) >= 10:
            top = 10
        else:
            top = len(top_domains)
        return [{"Domain": elem[0], "NumberOfRequests":elem[1]} for elem in Counter(top_domains).most_common(top)]



    
