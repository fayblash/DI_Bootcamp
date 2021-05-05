# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.
import requests
from datetime import timedelta 
# import datetime
# import time

urls=["https://www.bank-yahav.co.il/","https://www.meuhedet.co.il","https://www.imdb.com","https://www.ynet.co.il"]
times=[]

for url in urls:
    request_time=requests.get(url).elapsed.total_seconds()
    print(request_time)
    times.append(request_time)

#store request_time in persistent data store
request_dict=dict(zip(urls,times))
print(request_dict)