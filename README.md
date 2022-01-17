# Assignment-aggregation-system python
## The projects goal


Build aggregation system. 

* Creating an endpoint to receive the events and an endpoint to get each stats/one endpoint with parameters.

* tests for the assignment, .

### Requirements:

* Accept over http json objects (counters). Counter includes fields: 

  * {"timestamp": 1608102631, "A": 3, "B": 4}

  * "A" is a domain, and 3 is a number of requests domain got 

during 1608102631 (Unix epoch time)

* System should be able to show statistics​:

  * Top 10 domains last round minute (with several requests). If now 54min and 30 sec. We need stats for 53 minutes.

  * Top 10 domains last round hour (with several requests). Same logic as above 
  
 # Usage
  ## Start Server
  
  #### src/server.py 
  
      dviraz@DESKTOP-A9KS2MS/src$ python3 server.py
     
  ## Adding records 
    dviraz@DESKTOP-A9KS2MS$:curl -X POST 'http://localhost:5000/api/events -d {"timestamp": "1636030456", "A": 7, "B": 8, "C":65}
   
   
  ## Listing stats
  By minutes:
    GET /stats/minutes
                   
      dviraz@DESKTOP-A9KS2MS$ curl 'http://localhost:5000/stats/api/minutes
      [{"Domain":"C","NumberOfRequests":8},{"Domain":"B","NumberOfRequests":4},{"Domain":"A","NumberOfRequests":3}]
       
  By hours:
    GET /stats/hours
                       
    dviraz@DESKTOP-A9KS2MS$$ curl 'http://localhost:5000/stats/api/hours'     
    ["Domain":"D","NumberOfRequests":216},{"Domain":"V","NumberOfRequests":205},{"Domain":"I","NumberOfRequests":143},{"Domain":"R","NumberOfRequests":116},{"Domain":"A","NumberOfRequests":100},{"Domain":"Z","NumberOfRequests":99},{"Domain":"S","NumberOfReq
    uests":95},{"Domain":"E","NumberOfRequests":90},{"Domain":"K","NumberOfRequests":84},{"Domain":"W","NumberOfRequests":82}]
    
    
       
 ## Tests
 ### Unit test:
 #### test/test_statistics.py
    dviraz@DESKTOP-A9KS2MS/tests$ python3 test_statistics.py
 ### Integration test: 
 #### src/client.py
    dviraz@DESKTOP-A9KS2MS/src$ python3 client.py
    
    
 ### Author

    Dvir azami:
        github@dviraz90
