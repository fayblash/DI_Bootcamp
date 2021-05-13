import sqlite3 as sl
from time import time
import requests
import json

connection=sl.connect("countries.db")

cursor=connection.cursor()

start=time()

for i in range(10,21):
    data=requests.get("https://restcountries.eu/rest/v2/all")
    country=data.json()
    print (country[i]['name'])
    query=f"INSERT INTO countries(name,capital,flag,subregion,population) VALUES ('{country[i]['name']}','{country[i]['capital']}','{country[i]['flag']}','{country[i]['subregion']}','{country[i]['population']}')"
    cursor.execute(query)
    connection.commit() 
    
connection.close()    

end=time()

print(end-start)
